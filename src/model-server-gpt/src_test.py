from transformers import GPT2Tokenizer, GPT2LMHeadModel


def main():
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    text = "Yo my man!."
    encoded_input = tokenizer(text, return_tensors='pt')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    output = model.generate(**encoded_input, max_new_tokens=70)
    decoded = tokenizer.decode(output[0])
    print(decoded)


if __name__ == '__main__':
    main()
