# Documentation-Scraping-Conversion
Python script designed to scrape text from online documentation websites and convert the extracted content into PDF files.


Documentation Scraping and Conversion
This repository contains a set of Python scripts designed to scrape text from online documentation websites and convert the extracted content into PDF files. The main example provided here focuses on scraping the Tailwind CSS documentation, but the scripts are built to be reusable and can be applied to various documentation sources by adjusting the relevant selectors.

Script Overview
1. TailwindSpider.py
TailwindSpider.py is a Python script that utilizes Selenium WebDriver to scrape text from the Tailwind CSS documentation website. The script navigates through the pages, extracts the content, and saves each section as a separate text file. The filenames are sanitized to be used as file names. The script is designed to handle pagination, making it suitable for scraping lengthy documentation.

2. TextConv.py
TextConv.py converts the previously scraped text files into corresponding PDF files using the pdfkit library. It iterates through the collection of text files and generates PDFs with the same content. This step ensures that the extracted content is easily readable and shareable.

3. PdfMerger.py
PdfMerger.py is responsible for merging all the generated PDF files into a single comprehensive PDF document named tailwindDocs.pdf. It utilizes the PyPDF2 library to combine the individual PDFs into one cohesive file.

Usage
Clone this repository and navigate to the root directory.
Run TailwindSpider.py to scrape the Tailwind CSS documentation and create individual text files for each section. If you want to scrape a different documentation source, modify the selectors in the script to match the specific website's elements.
Execute TextConv.py to convert the text files into corresponding PDFs.
Finally, run PdfMerger.py to merge all the generated PDF files into a single comprehensive document.
Note
The provided scripts do not focus on perfect formatting since the PDFs are used in conjunction with a chatbot that understands tokens. The primary goal is to convert the documentation into a readable format that can be processed by AI bots.
Contributions
Contributions to this repository are highly appreciated! Feel free to improve the scripts, add support for different documentation sources, or optimize the code for better performance. Your contributions will make the project more versatile and valuable to the community.

Disclaimer
This project serves educational and personal purposes. Users are responsible for complying with the terms of service of the websites they scrape. The authors and contributors of this repository are not responsible for any misuse of the scripts or any consequences arising from it. Use the code responsibly and respect the policies of the websites you interact with.


Author: Assante Ahmad
Email: loukmanassante@outlook.com
