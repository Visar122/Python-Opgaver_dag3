import string

def acronyms(text):
   
    result = []
    
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
  
    for word in text.split():
     
        if len(word) >= 2 and word.isupper():
            result.append(word)
    
    return result

def main():
    text = """For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""
    
    # Call the acronyms function and print the result
    print(acronyms(text))

if __name__ == "__main__":
    main()
