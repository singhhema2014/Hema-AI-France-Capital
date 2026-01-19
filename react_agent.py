"""
Day 1: ReAct Agent from Scratch
Location: ~/Desktop/agentic-bootcamp/react_agent.py
"""

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

class ReActAgent:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=os.getenv('GROQ_API_KEY'),
            model="llama-3.1-8b-instant"
        )
        self.tools = {
            "search": self.dummy_search,
            "calculate": self.dummy_calculate
        }
        self.memory = []
    
    def dummy_search(self, query):
        """Fake search tool - real mein web search hoga"""
        return f"Search result for '{query}': Found relevant info!"
    
    def dummy_calculate(self, expression):
        """Fake calculator - real mein math.js hoga"""
        try:
            return str(eval(expression))
        except:
            return "Calculation error"
    
    def parse_action(self, text):
        """Action extract karta hai: "search: weather Delhi" → ("search", "weather Delhi")"""
        if "search:" in text.lower():
            return "search", text.split("search:", 1)[1].strip()
        elif "calculate:" in text.lower():
            return "calculate", text.split("calculate:", 1)[1].strip()
        return None, None
    
    def run(self, question, max_steps=5):
        print(f"\n🤖 Question: {question}")
        self.memory = [{"role": "user", "content": question}]
        
        for step in range(max_steps):
            print(f"\n--- Step {step + 1} ---")
            
            # LLM ko full context do
            messages = self.memory.copy()
            prompt = self.get_react_prompt()
            messages.insert(0, {"role": "system", "content": prompt})
            
            response = self.llm.invoke(messages)
            thought = response.content
            
            print(f"💭 Thought: {thought}")
            self.memory.append({"role": "assistant", "content": thought})
            
            # Action parse karo
            action, action_input = self.parse_action(thought)
            if action and action_input:
                print(f"🔧 Action: {action}({action_input})")
                
                # Tool execute karo
                observation = self.tools[action](action_input)
                print(f"📊 Observation: {observation}")
                self.memory.append({"role": "system", "content": f"Observation: {observation}"})
            else:
                print("✅ Final Answer!")
                return thought
        
        return "Max steps reached!"

    def get_react_prompt(self):
        return """
You are a ReAct Agent. Follow this EXACT format:

1. Thought: Reason step-by-step what to do
2. Action: Use ONE tool - search:query OR calculate:expression
3. PAUSE after Action

Available tools:
- search:weather Delhi (returns search results)
- calculate:25*4+10 (returns math result)

When you have the answer, say "Final Answer: [answer]"

Example:
Question: What is 25*4?
Thought: I need to calculate 25*4
Action: calculate:25*4
PAUSE
"""

# Test agent
if __name__ == "__main__":
    agent = ReActAgent()
    result = agent.run("What is the capital of France?")
    print(f"\n🎉 Final Result: {result}")
