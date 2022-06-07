from .Document import Document
from services.text_processing import *

class Collection:


    def __init__(self, file_name,file_stopWord):
        self._file_name = file_name
        self._file_stopWord =file_stopWord

    def read_file_collection(self):
        file_collection = open(self._file_name, "r")
        file_content = file_collection.read()
        file_collection.close()
        return file_content

    def createDoc(self, document, contentTag, currentTag,content) :
        if currentTag == ".T":
            document.T = " ".join(contentTag)
            document.Content = " ".join(content)
        elif currentTag == ".B":
            document.B = " ".join(contentTag)
            document.Content = " ".join(content)
        elif currentTag == ".A":
            document.A = " ".join(contentTag)
            document.Content = " ".join(content)
        elif currentTag == ".N":
            document.N = " ".join(contentTag)
        elif currentTag == ".K":
            document.K = " ".join(contentTag)
        elif currentTag == ".X":
            document.X = " ".join(contentTag)
        elif currentTag == ".W":
            document.W = " ".join(contentTag)
            document.Content = " ".join(content)

        else:
            print("Error")
        
    def parser(self) :
        file_content=self.read_file_collection()
        documents = {}
        if not file_content :
            print("Error. content not exist.")
        else :
            split_content = file_content.split(".I ")

            new_split_content = split_content[1:]
       
            Tag = [".T",".B",".A",".N",".W",".X",".K"]
            
            for doc in new_split_content :
                document = Document()
                currentTag = ""
                contentTag = []
                content = []
                
                lines = doc.splitlines()
                document.I = lines[0]
                
                for i in range(1,len(lines)) :
                    if lines[i] in Tag :
                        if not currentTag :
                            currentTag = lines[i]
                        else :
                            self.createDoc(document, contentTag, currentTag,content)
                            contentTag = []
                            currentTag = lines[i]
                    else :
                        contentTag.append(lines[i])
                        if currentTag == ".T":
                            content.append(lines[i])
                        if currentTag == ".B":
                            content.append(lines[i])
                        if currentTag == ".A":
                            content.append(lines[i])
                        if currentTag == ".W":
                            content.append(lines[i])

                self.createDoc(document, contentTag, currentTag,content)
                documents[document.I] = document

            return documents

    # return list of documents without processing
    def get_content_collection(self):
        collection=self.parser()
        documents = []
        for i,doc in collection.items():
            documents.append(doc.Content)
        return documents

    # return list of documents with processing
    def get_process_collection(self):
        collection=self.parser()
        proc_documents = []
        for i,doc in collection.items():
            proc_documents.append(doc.processing_content(self._get_stop_word()))
        return proc_documents

    def _get_file_name(self):
        return self._file_name
    
    def _set_file_name(self, newName):
        self._file_name = newName

    def _get_file_stopWord(self):
        return self._file_stopWord

    def _set_file_stopWord(self, newStopWord):
        self._file_stopWord = newStopWord

    def _get_stop_word(self):
        with open(self._file_stopWord) as f:
            stop_word = f.readlines()
        stop_word = [x.strip() for x in stop_word]
        return stop_word

