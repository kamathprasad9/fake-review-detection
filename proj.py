import torch
import streamlit as st
from transformers import BertTokenizer
from transformers import BertForSequenceClassification
from load_css import local_css
# from proj1 import * as proj1
# import db_proj as db

local_css("style.css")

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
model=BertForSequenceClassification.from_pretrained("bert-base-uncased",num_labels=1,output_attentions=False,output_hidden_states=False)
model.dropout.p=0.5
loaded_checkpoint=torch.load("./BERT_committed_2_32_0.00001.pth",map_location=torch.device('cpu'))
model.load_state_dict(loaded_checkpoint["model_state"])

def classify(sentence, model):
    encoded_dictionary=tokenizer.encode_plus(sentence, add_special_tokens=True, max_length=320, truncation=True, padding='max_length', return_attention_mask=True)
    #Returns a dictionary having, keys - 'input_ids','token_type_ids','attention_mask'
    output=model(input_ids=torch.tensor(encoded_dictionary["input_ids"]).unsqueeze(0),attention_mask=torch.tensor(encoded_dictionary["attention_mask"]).unsqueeze(0))
    output_p=torch.sigmoid(output.logits).view(-1)
    return output_p

# model = None

# run_once=0
# if(not run_once):
#     model=makeModel()
#     run_once=1

st.title("Fake Review Detection")
sentence = st.text_area("Enter the review")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = classify(sentence,model)
    #   threshold=0.6
    if (result>=0.5):
        ans = f"<div>With a confidence of <span class='blue bold'>{result.item()*100:.2f}%</span>, the model considers the review to be a <span class='blue bold'>fake</span> review.<div>"

        # db.appendInfo(sentence, round(result.item()*100,2), 'Fake')
    else:
        ans =  f"<div>With a confidence of <span class='blue bold'>{(1-result.item())*100:.2f}%</span>, the model considers the review to be a <span class='blue bold'>genuine</span> review.</div>"

        # db.appendInfo(sentence, round((1-result.item())*100,2), 'Genuine')
    st.markdown(ans, unsafe_allow_html=True)

# st.write("Prediction dependency: 80%")

# st.write("This BERT model was trained on YELP Reviews using PyTorch")
# rows=db.readData()
# print(rows)
# if(len(rows)):
#     if st.checkbox('Show History'):
#         st.subheader('Center Information data')
#         st.write(rows)
#     else:
#         st.write()
