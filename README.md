# personality sim chatbot
fine tune an llm on your text using lora and quantization

# how to do

note: some code may need to be modified based on the structure and type of your texts

# step 1
you can use any source of text you'd like, i choose to use my discord messages since i have a lot of them and that's probably closest to my "true" voice. 

to process your discord data, run python process.py

# step 2 
tokenizing the data. from now on, my code is being run on runpod 4x A100, but you can also run it on your local computre. run tokenize_documents.ipynb

# step 3
to finetune run finetune.ipynb 
your finetuned model should now be saved where you wanted it to be

now you can test talking to it in evaluate.ipynb
<img width="851" alt="Screenshot 2024-08-30 at 2 03 14 PM" src="https://github.com/user-attachments/assets/702d2004-6744-4200-9d6f-f45d1006e539">
