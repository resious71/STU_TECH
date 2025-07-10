LangChain 기초

== 커리귤럼 ==
1. 체인(chain)에 대한 이해: 기본 LLM 체인(Prompt + LLM) | 멀티 체인
2. 프롬프트 만들기: Prompt Template 이해 및 적용
3. LLM 모델 구조: LLM 클래스와 ChatModel 모델 클래스 구분
4. LLM 모델 튜닝: 모델 파라미터(model parameter) 설정
5. RAG 기법 이해: 웹 문서에 대한 qb 챗봇 만들기


== 개발환경 ==
- 파이썬: 3.11 (3.10.0 이상, 3.12 미만
- LangChain: 0.1.10 
- OpenAI: GPT-3.5-turbo-0125
- 코드 에디터: 구글 Colab
- 실습 파일: https://github.com/tsdata/langchain-study

1) 라이브러리 설치 
   >> !pip install -q langchain langchain-openai tiktoken
2) OpenAI 인증키 설정
   >> os.environ['OPEN_API_KEY'] = 'OPEN_API_KEY'

++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++ 1. 체인(chain)에 대한 이해: 기본 LLM 체인(Prompt + LLM) | 멀티 체인 +++
++++++++++++++++++++++++++++++++++++++++++++++++++++++

@@ 기본 체인 (Prompt + LLM)

   - 가장 기본적이고 일반적인 사용 사례
   - 프롬프트 템플릿과 모델을 연결
   - Format --> Predict --> Parse (https://python.langchain.com)        

  ==> 구성요소
           + 1) 프롬프트: 입력, LLM에게 특정 작업을 수행하도록 요청하는 지시문
           + 2) LLM: 언어 모델, 프롬프트를 바탕으로 응답 생성, 작업 수행

  ==> 일반적인 작동방식 
              1) 프롬프트 생성 --> 2) LLM 처리  --> 3) 응답 반환

##########################################################
  from langchain_openai import ChatOpenAI

  # model
  llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
  
  # chain 실행
  result = llm.invoke("지구의 자전 주기는?")
  print(result)         # 반복하면 답이 달라진다.
 
##########################################################
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser

  # prompt + model + output parser
  prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")
  llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
  output_parser = StrOutputParser()

  # LCEL chaining
  chain = prompt | llm | output_parser

  # chain 호출 
  chain.invoke({"input":"지구의 자전 주기는?"})

@@ Multiple Chains 
  
    - 여러 개의 체인을 사용 (2개 이상)
   
##########################################################
 
 prompt1 = ChatPromptTemplate.from_template("translates {korean_word} to English.")
 prompt2 = ChatPromptTemplate.from_template("
          explain {english_word} using oxford dictionary to me in korean."
 )

 lim = ChatOpenAI(model="gpt-3.5-turbo-0125")
 chain1 = prompt1 | llm | StrOutputParser()
 chain1.invoke("korean_word":"미래"

 chain2 = (
       {"english_word": chain1}
       | prompt2
       | llm
       | StrOutputParser()
 )
 
 chain2.invoke({"korean_word":"미래"})  


++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++ 2. 프롬프트 만들기: Prompt Template 이해 및 적용                        +++
++++++++++++++++++++++++++++++++++++++++++++++++++++++

 - 프롬프트: 사용자와 언어 모델 간의 대화에서 질문이나 요청의 형태로 제시되는 입력문
 - 랭체인 --> 프롬프트 템플릿 사용
 - PromptTemplate : 단일 문장 또는 간단한 응답을 생성하는데 사용
     + 파이선의 문자열 포맷팅 사용 가능, 동적으로 위치 지정 가능

 >> !pip install -q langchain lanchain-openai tiktoken

  1) PromptTemplate
      + PromptTemplate + LLMs(단일 문장 입력 -> 단일 문장 출력)
      + 문자열 프롬프트를 위한 템플릿 생성, 파이썬의 문자열 포맷팅 구문을 사용
      + 내용: 지시, 몇 가지 예시, 특정 맥락 및 질문 등

##########################################################

 from langchain_core.prompts import PromptTemplate

 # 'name'과 'age'라는 두 개의 변수를 사용하는 프롬프트 템플릿을 정의
 template_text = "안녕하세요, 제 이름은 {name}이고, 나이는 {age}살입니다"

 # PromptTemplate 인스턴스를 생성
 prompt_template = PromptTemplate.from_template(template_text)

 # 템플릿에 값을 채워서 프롬프트를 완성
 filled_prompt = prompt_template.fromat(name="홍길동", age=30)

 print(filled_prompt)

 # 문자열 템플릿 결함 (PromptTemplate + PromptTemplate + 문자열)
 combined_prompt = (
       prompt_template
       + PromptTemplate.from_template("\n\n 아버지를 아버지라 부를 수 없습니다.")
       + "\n\n {language}로 번역해 주세요."      
  )

 print(combined_prompt)

 combined_prompt.format(name="홍길동", age=30, language="영어")

 from langchain_openai import ChatOpenAI
 from langchain_core.output_parsers import StrOutputParser

 llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
 chain = combined_prompt | llm | StrOutputParser()
 chain.invoke({"age":30, "language": "영어", "name": "홍길동"})

  2) ChatPromptTemplate
      + 대화형 상황에서 여러 메시지 입력 기반으로 단일 메시지 응답을 생성
      + 대화형 모델이나 챗봇 개발에 사용
      + 입력: 여러 메시지를 원소로 갖는 리스트, 각 메시지는 역할(Role)과 내용(Content)로 구성  

      -- Message 유형
         + SystemMessage: 시스템의 기능 설명
         + HumanMessage: 사용자 질문
         + AIMessage: AI 모델의 응답
         + FunctionMessage: 특정 함수 호출의 결과 
         + ToolMessage: 도구 호출의 결과 

     -- ChatPromptTemplate
         + ChatPromptTemplates + ChatModels (여러 메시지 입력 --> 단일 메시지 출력)
         + 채팅 메시지를 원소로 갖는 리스트 형태
         + 구성: 각 채팅 메시지는 역할(role)과 내용(content)이 짝을 이루는 형태
             ++ 예시: OpenAI는 AI Assistant, Human, System 등의 역할(role)로 구성

##########################################################

 # 2-튜플 형태의 메시지 목록으로 프롬프트 생성(type, content)
   from langchain_core.prompts import PromptTemplate

  chat_prompt = ChatPromptTemplate.from_message([
         ("system", "이 시스템은 천문학 질문에 답변할 수 있습니다."),
         ("user", "{user_input}),  
   ])

  message = chat_prompt.format_message(user_input="태양계에서 가장 큰 행성은 무엇인가요?"),
  print(message)

  chain = chat_prompt | llm | StrOutputParser()
  chain.invoke("{"user_input": "태양계에서 가장 큰 행성은 무엇인가요?}")  



  from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
  
  chat_prompt = ChatPromptTemplate.from_message(
       [
            SystemMessagePromptTemplate.from_template("이 시스템은 천문학 질문에 답변할 수 있습니다."),    

       ]
  )

  message = chat_prompt.format_message(user_input = "태양계에서 가장 큰 행성은 무엇인가요?")
  message   


++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++ 3. LLM 모델 구조: LLM 클래스와 ChatModel 모델 클래스 구분           +++
++++++++++++++++++++++++++++++++++++++++++++++++++++++



++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++ 4. LLM 모델 튜닝: 모델 파라미터(model parameter) 설정                  +++
++++++++++++++++++++++++++++++++++++++++++++++++++++++




++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++ 5. RAG 기법 이해: 웹 문서에 대한 qb 챗봇 만들기                          +++
++++++++++++++++++++++++++++++++++++++++++++++++++++++





