# Agentic Bootcamp - Day 1
## ReAct Pattern Notes (YouTube: "Build an AI Agent From Scratch")

**ReAct Pattern**: Observe → Reason → Act → Repeat
**Agent ≠ Chatbot**: 
- Chatbot: It only generates text
- Agent: It uses TOOLS (search, calculator, etc.)

**Core Loop**:
1. Thought (what is the plan)
2. Action (Which tool) 
3. Observation (What is the result of tool)
4. Repeat till you get results

**Status**: ✅ Environment ready | ⏳ Building first agent...
EOFfrom dotenv import load_dotenv 

from langchain_openai import ChatOpenAI 

from langchain_core.prompts import ChatPromptTemplate 

load_dotenv() 

  

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) 

prompt = ChatPromptTemplate.from_template("Think step-by-step: {task}") 

chain = prompt | llm 

  

print(chain.invoke({"task": "Explain agentic AI in Dublin weather terms"})) 
hi
uit
quit
q
o



cd



exit
exit 1
cat <<EOF
