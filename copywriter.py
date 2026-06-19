import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")

def generate_copy(product_name, platform, tone, temperature=0.7, top_p=0.9):
    
    prompt = f"""
You are a professional marketing copywriter. Your task is to generate platform-specific marketing copy for a product.

Product Name: {product_name}
Platform: {platform}
Tone: {tone}

Instructions:
- Write a compelling, engaging copy suitable for the specified platform.
- Match the tone exactly as specified.
- Keep it concise and impactful.
- Do not include any extra text or explanations.

Copy:
"""
    
    model = genai.GenerativeModel(
        "gemini-1.5-pro",
        generation_config={
            "temperature": temperature,
            "top_p": top_p,
        }
    )
    
    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    print("\n" + "=" * 60)
    print("   AUTOMATED COPYWRITING & TONE TRANSFORMER")
    print("=" * 60)
    print("\nEnter product details to generate marketing copy.\n")
    
    product_name = input("Product Name: ")
    platform = input("Platform (LinkedIn/Instagram/Email): ")
    tone = input("Tone (Professional/Casual/Playful/Formal): ")
    
    print("\n" + "-" * 60)
    print("GENERATED COPY")
    print("-" * 60)
    
    copy = generate_copy(product_name, platform, tone)
    print("\n" + copy + "\n")
    
    print("-" * 60)
    print("\nTrying with different temperature settings:\n")
    
    print("Temperature 0.3 (Conservative):")
    print("-" * 40)
    copy_low = generate_copy(product_name, platform, tone, temperature=0.3)
    print(copy_low + "\n")
    
    print("Temperature 1.2 (Creative):")
    print("-" * 40)
    copy_high = generate_copy(product_name, platform, tone, temperature=1.2)
    print(copy_high + "\n")
    
    print("=" * 60)
    print("   COPY GENERATION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()