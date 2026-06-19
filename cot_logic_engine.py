import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")

def solve_with_cot(problem):
    prompt = f"""
You are a logical reasoning assistant. Your task is to solve the given problem using explicit step-by-step reasoning.

Instructions:
1. Read the problem carefully.
2. Break down the problem into logical steps.
3. Show each step of your reasoning clearly.
4. After completing all steps, state the final answer.
5. Do not skip any steps or make assumptions.
6. Review your work for errors.

Problem:
{problem}

Step-by-Step Reasoning:
"""

    model = genai.GenerativeModel(
        "gemini-1.5-pro",
        generation_config={
            "temperature": 0.0,
            "top_p": 1.0,
        }
    )

    response = model.generate_content(prompt)
    return response.text.strip()

def solve_with_self_correction(problem):
    prompt = f"""
You are a logical reasoning assistant. Your task is to solve the given problem using explicit step-by-step reasoning with self-correction.

Instructions:
1. Read the problem carefully.
2. Break down the problem into logical steps.
3. Show each step of your reasoning clearly.
4. After completing all steps, state the final answer.
5. Now review your reasoning for any errors, assumptions, or leaps in logic.
6. If you find an error, correct it and provide the revised answer.

Problem:
{problem}

Step-by-Step Reasoning:
"""

    model = genai.GenerativeModel(
        "gemini-1.5-pro",
        generation_config={
            "temperature": 0.0,
            "top_p": 1.0,
        }
    )

    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    print("\n" + "=" * 60)
    print("   CHAIN-OF-THOUGHT LOGIC ENGINE")
    print("=" * 60)

    problems = [
        "A farmer has 17 sheep. All but 9 die. How many are left?",
        "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?",
        "If you have a 5-liter jug and a 3-liter jug, how can you measure exactly 4 liters of water?",
        "Three doctors said that Robert was their brother. Robert said he had no brothers. Who is lying?",
        "What comes next in the sequence: 1, 1, 2, 3, 5, 8, ?"
    ]

    for i, problem in enumerate(problems, 1):
        print("\n" + "=" * 60)
        print(f"PROBLEM {i}:")
        print("=" * 60)
        print(problem)

        print("\n[1] Standard CoT Reasoning:")
        print("-" * 60)
        result = solve_with_cot(problem)
        print(result)

        print("\n[2] CoT with Self-Correction:")
        print("-" * 60)
        result_corrected = solve_with_self_correction(problem)
        print(result_corrected)

        print("\n" + "=" * 60)

    print("\n" + "=" * 60)
    print("   COT LOGIC ENGINE COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()