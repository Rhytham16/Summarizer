{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "8e184d82-a9ac-41dd-86f7-a49c5a3950e8",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'env'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[48], line 7\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlangchain\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mprompts\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m PromptTemplate\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mos\u001b[39;00m\n\u001b[1;32m----> 7\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01menv\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m OPENAI_API_KEY\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'env'"
     ]
    }
   ],
   "source": [
    "from PyPDF2 import PdfReader\n",
    "from langchain.chat_models import ChatOpenAI\n",
    "from langchain.text_splitter import RecursiveCharacterTextSplitter\n",
    "from langchain.prompts import PromptTemplate\n",
    "import os\n",
    "\n",
    "from env import OPENAI_API_KEY"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "5d4d2c3e-d4e0-40f5-8463-e6a14b68caac",
   "metadata": {},
   "outputs": [],
   "source": [
    "os.environ[\"OPENAI_API_KEY\"]= OPENAI_API_KEY\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "89b5ae81-6db9-4882-83f0-78b65244ea0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def extract_text_from_pdf(file_path):\n",
    "    reader = PdfReader(file_path)\n",
    "    text = \"\"\n",
    "    for page in reader.pages:\n",
    "        page_text = page.extract_text()\n",
    "        if page_text:\n",
    "            text += page_text\n",
    "    return text\n",
    "\n",
    "\n",
    "pdf_text = extract_text_from_pdf(\"Unit- I. Number Theorem.pdf\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "9ddc238a-8929-46b7-9a22-6ea168b00f91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total chunks created: 7\n"
     ]
    }
   ],
   "source": [
    "splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)\n",
    "chunks = splitter.split_text(pdf_text)\n",
    "\n",
    "print(f\"Total chunks created: {len(chunks)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "627c5edc-e827-4dfe-bbe7-57773c853eaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the number 653xy such that this \n",
      "number is divisible by 80, then x + \n",
      "y =? \n",
      "A) 4 \n",
      "B) 4 or 8  \n",
      "C) 2 or 6  \n",
      "D) 8 \n",
      "7. What should come in place x if \n",
      "4857x is divisible by 88?   \n",
      "A) 2 \n",
      "B) 8 \n",
      "C) 4 \n",
      "D) 6 \n",
      "8. If the product 4864 x 9 P 2 is \n",
      "divisible by 12, then the value of P \n",
      "is: \n",
      "A) 5 \n",
      "B) 8 \n",
      "C) 2 \n",
      "D) None  \n",
      " 9. The unit digit in the product \n",
      "(122)173   is: \n",
      "A) 2 \n",
      "B) 4 \n",
      "C) 6 \n",
      "D) 8 \n",
      "10. Find the unit digit in the \n",
      "product (4387)245 × (621)72. \n",
      "A) 1 \n",
      "B) 2 \n",
      "C) 5 \n",
      "D) 7 \n",
      "11. What is the unit digit in  \n",
      "(2538)212. \n",
      "A) 8 \n",
      "B) 1 \n",
      "C) 6 \n",
      "D) 4 \n",
      "12. What is the unit digit in 240. \n",
      "A) 0 \n",
      "B) 1 \n",
      "C) 2 \n",
      "D) 6 \n",
      "13. What is the unit digit in  \n",
      "(69!)646? \n",
      "A) 1 \n",
      "B) 9 \n",
      "C) 0 \n",
      "D) None  \n",
      "14. What is the unit digit in  \n",
      "(795 - 358)? \n",
      "A) 0 \n",
      "B) -6 \n",
      "C) 4 \n",
      "D) 7 \n",
      "15. The unit digit in the sum of \n",
      "(123)53!  \n",
      "A) 3 \n",
      "B) 9 \n",
      "C) 0 \n",
      "D) 1 \n",
      "16. The digit in the unit position of \n",
      "the integer 1! + 2! + 3! + …+99! Is \n",
      "A) 3 \n",
      "B) 0 \n",
      "C) 1 \n",
      "D) 7 \n",
      "17. Find the number of factors of \n",
      "144?  \n",
      "A) 15 \n",
      "B) 12 \n",
      "C) 8 \n",
      "D) None\n"
     ]
    }
   ],
   "source": [
    "print(chunks[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "305372d9-142d-47f0-8dfe-9579910f0fbf",
   "metadata": {},
   "outputs": [
    {
     "ename": "OpenAIError",
     "evalue": "The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOpenAIError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[47], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m llm \u001b[38;5;241m=\u001b[39m \u001b[43mChatOpenAI\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmodel\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mgpt-3.5-turbo\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtemperature\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m0\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21msummarize_chunk\u001b[39m(chunk):\n\u001b[0;32m      4\u001b[0m     prompt \u001b[38;5;241m=\u001b[39m PromptTemplate(\n\u001b[0;32m      5\u001b[0m         input_variables\u001b[38;5;241m=\u001b[39m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m      6\u001b[0m         template\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPlease summarize the following text:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;132;01m{text}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m      7\u001b[0m     )\n",
      "File \u001b[1;32m~\\Lib\\site-packages\\langchain_core\\load\\serializable.py:130\u001b[0m, in \u001b[0;36mSerializable.__init__\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    128\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__init__\u001b[39m(\u001b[38;5;28mself\u001b[39m, \u001b[38;5;241m*\u001b[39margs: Any, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs: Any) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    129\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"\"\"\"\u001b[39;00m  \u001b[38;5;66;03m# noqa: D419\u001b[39;00m\n\u001b[1;32m--> 130\u001b[0m     \u001b[38;5;28;43msuper\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[38;5;21;43m__init__\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "    \u001b[1;31m[... skipping hidden 1 frame]\u001b[0m\n",
      "File \u001b[1;32m~\\Lib\\site-packages\\langchain_openai\\chat_models\\base.py:690\u001b[0m, in \u001b[0;36mBaseChatOpenAI.validate_environment\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    683\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhttp_client \u001b[38;5;241m=\u001b[39m httpx\u001b[38;5;241m.\u001b[39mClient(\n\u001b[0;32m    684\u001b[0m             proxy\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mopenai_proxy, verify\u001b[38;5;241m=\u001b[39mglobal_ssl_context\n\u001b[0;32m    685\u001b[0m         )\n\u001b[0;32m    686\u001b[0m     sync_specific \u001b[38;5;241m=\u001b[39m {\n\u001b[0;32m    687\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhttp_client\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhttp_client\n\u001b[0;32m    688\u001b[0m         \u001b[38;5;129;01mor\u001b[39;00m _get_default_httpx_client(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mopenai_api_base, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mrequest_timeout)\n\u001b[0;32m    689\u001b[0m     }\n\u001b[1;32m--> 690\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mroot_client \u001b[38;5;241m=\u001b[39m \u001b[43mopenai\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mOpenAI\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mclient_params\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43msync_specific\u001b[49m\u001b[43m)\u001b[49m  \u001b[38;5;66;03m# type: ignore[arg-type]\u001b[39;00m\n\u001b[0;32m    691\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mclient \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mroot_client\u001b[38;5;241m.\u001b[39mchat\u001b[38;5;241m.\u001b[39mcompletions\n\u001b[0;32m    692\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39masync_client:\n",
      "File \u001b[1;32m~\\Lib\\site-packages\\openai\\_client.py:126\u001b[0m, in \u001b[0;36mOpenAI.__init__\u001b[1;34m(self, api_key, organization, project, base_url, websocket_base_url, timeout, max_retries, default_headers, default_query, http_client, _strict_response_validation)\u001b[0m\n\u001b[0;32m    124\u001b[0m     api_key \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mOPENAI_API_KEY\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    125\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m api_key \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m--> 126\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m OpenAIError(\n\u001b[0;32m    127\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    128\u001b[0m     )\n\u001b[0;32m    129\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mapi_key \u001b[38;5;241m=\u001b[39m api_key\n\u001b[0;32m    131\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m organization \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[1;31mOpenAIError\u001b[0m: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable"
     ]
    }
   ],
   "source": [
    "llm = ChatOpenAI(model_name=\"gpt-3.5-turbo\", temperature=0)\n",
    "\n",
    "def summarize_chunk(chunk):\n",
    "    prompt = PromptTemplate(\n",
    "        input_variables=[\"text\"],\n",
    "        template=\"Please summarize the following text:\\n{text}\"\n",
    "    )\n",
    "    formatted_prompt = prompt.format(text=chunk)\n",
    "    return llm.predict(formatted_prompt)\n",
    "\n",
    "summaries = [summarize_chunk(chunk) for chunk in chunks]\n",
    "full_summary = \"\\n\\n\".join(summaries)\n",
    "\n",
    "print(full_summary)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21377d15-4832-4eeb-89a3-2b7cb22e745d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60e64dc6-3cc1-437e-8774-9cca13da677a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fd0954c-c057-421e-8e1b-06cba5afd42f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
