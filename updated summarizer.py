{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8f80518b-f182-4810-88d0-50ee000439ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "import fitz  \n",
    "import os\n",
    "import json\n",
    "from dotenv import load_dotenv\n",
    "from langchain_openai import ChatOpenAI\n",
    "from langchain.prompts import PromptTemplate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c8a6eb60-b976-4e0f-bead-41cc6cb7c93d",
   "metadata": {},
   "outputs": [],
   "source": [
    "load_dotenv(\"D:\\Langchain\\summary\\.env.txt\")\n",
    "llm = ChatOpenAI(model=\"gpt-3.5-turbo\", temperature=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8d51cdde-3af9-4d4c-b7ca-249b9f35bba0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def extract_pages_text(pdf_path, page_numbers):\n",
    "    \n",
    "    \"\"\"Extract text from specific pages of a PDF.\n",
    "\n",
    "    Args:\n",
    "        pdf_path (str): The file path to the PDF document.\n",
    "        page_numbers (list): List of zero-indexed page numbers to extract.\n",
    "\n",
    "    Returns:\n",
    "        str: Combined text content from the specified pages.\n",
    "    \"\"\"\n",
    "    \n",
    "    doc = fitz.open(pdf_path)\n",
    "    combined_text = \"\"\n",
    "    for num in page_numbers:\n",
    "        if 0 <= num < len(doc):\n",
    "            combined_text += doc.load_page(num).get_text()\n",
    "    return combined_text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b487530f-b551-4078-af5b-6e26a38adfab",
   "metadata": {},
   "outputs": [],
   "source": [
    "def summarize_text(text, instruction=\"Please summarize this content:\"):\n",
    "    \n",
    "     \"\"\"Summarize the given text using a language model with a given instruction.\n",
    "\n",
    "    Args:\n",
    "        text (str): The text content to summarize.\n",
    "        instruction (str, optional): The instruction prompt for summarization. Defaults to \"Please summarize this content:\".\n",
    "\n",
    "    Returns:\n",
    "        str: The generated summary from the LLM.\n",
    "    \"\"\"\n",
    "    \n",
    "    prompt = PromptTemplate(\n",
    "        input_variables=[\"instruction\", \"text\"],\n",
    "        template=\"{instruction}\\n\\n{text}\"\n",
    "    )\n",
    "    formatted_prompt = prompt.format(instruction=instruction, text=text)\n",
    "    return llm.invoke(formatted_prompt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "00a0e0b6-b5a8-4a54-9ce1-c4f351e44165",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Summary:\n",
      " content='The content is about the benefits of practicing mindfulness, including improved focus, reduced stress, and increased emotional regulation. It also discusses how mindfulness can help individuals become more present and aware in their daily lives.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 40, 'prompt_tokens': 12, 'total_tokens': 52, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-BmJ1PNZcuxUVUSZ2u0VsqcZHr3PR5', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--feb6a72e-35b1-4402-9722-4fb1ab73220e-0' usage_metadata={'input_tokens': 12, 'output_tokens': 40, 'total_tokens': 52, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}\n"
     ]
    }
   ],
   "source": [
    "pdf_path = \"Unit- I. Number Theorem.pdf\"\n",
    "selected_pages = [2, 3, 4]  # Pages 3, 4, 5 (0-indexed)\n",
    "text_to_summarize = extract_pages_text(pdf_path, selected_pages)\n",
    "\n",
    "summary = summarize_text(text_to_summarize)\n",
    "print(\"Summary:\\n\", summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "df7658a1-2b99-45a5-ab05-c1100fa7c933",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Summary saved to summary_output.json\n"
     ]
    }
   ],
   "source": [
    "output_data = {\n",
    "    \"pdf_file\": pdf_path,\n",
    "    \"pages_summarized\": [p + 1 for p in selected_pages], \n",
    "    \"summary\": str(summary)\n",
    "}\n",
    "\n",
    "with open(\"summary_output.json\", \"w\", encoding=\"utf-8\") as f:\n",
    "    json.dump(output_data, f, ensure_ascii=False, indent=4)\n",
    "\n",
    "print(\"Summary saved to summary_output.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4de3bf3-a0f7-4bfb-8475-1a25383c371a",
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
