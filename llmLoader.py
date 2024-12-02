# vllm_service.py
from flask import Flask, request, jsonify
from calculator import  calculatorAgent
form calculator import CalculatorAgent
import json
import vllm

app = Flask(__name__)
calc_agent = CalculatorAgent()

# Function to load the LLaMA model
def load_llama_model(model_path):
    model = vllm.LLM(model_path)
    return model

# Function to call the LLaMA model
def call_llama_model(model, input_text):
    result = model.generate(input_text)
    return result

# Load the LLaMA model from a local file
model_path = "/path/to/llama-3.1-8b"
llama_model = load_llama_model(model_path)

# Function to parse and call the appropriate CalculatorAgent function
def call_calculator_function(expression):
    try:
        result = calc_agent.evaluate_expression(expression)
        return result
    except ValueError as e:
        return str(e)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression')
    try:
        result = calc_agent.evaluate_expression(expression)
        return jsonify({"expression": expression, "result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/llm_call', methods=['POST'])
def llm_call():
    data = request.json
    input_text = data.get('input_text')
    
    # Call the LLaMA model to get the response
    llm_response = call_llama_model(llama_model, input_text)
    
    # Extract the expression from the LLaMA model's response
    # This assumes the model returns a JSON object with the expression
    response_dict = json.loads(llm_response)
    expression = response_dict.get('expression', '')
    
    if expression:
        # Call the calculator function with the extracted expression
        result = call_calculator_function(expression)
        return jsonify({"response": llm_response, "calculation_result": result})
    else:
        return jsonify({"response": llm_response, "error": "No expression found in LLM response"}), 400

if __name__ == '__main__':
    app.run(debug=True)
