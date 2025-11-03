import tiktoken


msg="Hi there, Myself Shushanth";

#creating the environment
enc=tiktoken.encoding_for_model("gpt-4o");

enc_result=enc.encode(msg);

print("Encoding text : ",enc_result);

dec_result=enc.decode([12194, 1354, 11, 197617, 1955, 1776, 66749]);

print(f"Decoding text : ",dec_result);