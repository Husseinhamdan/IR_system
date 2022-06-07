from textblob.en import Spelling
from textblob import TextBlob
import re
from model.query import Query


class Query_Collection:

    def __init__(self, query_file,query_relFile):
        self._query_file = query_file
        self._query_relFile = query_relFile

    def read_file_query(self):
        file_query = open(self._query_file, "r")
        file_query_content = file_query.read()
        file_query.close()
        return file_query_content

    def read_rel_file_query(self):
        with open(self._query_relFile) as f:
            file= f.read()
            relation_query=file.splitlines()
        return relation_query


    def CreatQuery(self, query, contentTag, currentTag):
      if currentTag == ".W":
            query.Name = " ".join(contentTag)

    def parser(self):
        queries = {}
        file_query=self.read_file_query()
        if not file_query:
            print("Error. content not exist.")
        else:
            split_content_query= file_query.split(".I ")
            relation_query = self.read_rel_file_query()
            new_split_content = split_content_query[1:]
            Tag = [".W"]
            for req in new_split_content:
                query = Query()
                currentTag = ""
                contentTag = []
                lines = req.splitlines()
                query.ID = lines[0]
                for i in range(1, len(lines)):
                    if lines[i] in Tag:
                        if not currentTag:
                            currentTag = lines[i]
                        else:
                            self.CreatQuery(query, contentTag, currentTag)
                            contentTag = []
                            currentTag = lines[i]
                    else:
                        contentTag.append(lines[i])
                self.CreatQuery(query, contentTag, currentTag)
                queries[query.ID] = query
            for line in relation_query:
                tokens = line.split()
                idQuery = int(tokens[0])
                idDocRel = tokens[1]
                queries[str(idQuery)].Relation.append(idDocRel)
            return queries

    def Spell_check_query(self,query):
        textToLower = ""
        with open("dataset/cacm/query.text", "r") as f1:
            text = f1.read()
            textToLower = text.lower()

        words = re.findall("[a-z]+", textToLower)
        oneString = " ".join(words)
        pathToFile = "dataset/trainSpellQuery.txt"
        spelling = Spelling(path=pathToFile)
        spelling.train(oneString, pathToFile)
        words = query.split()
        corrected = " "
        for i in words:
            corrected = corrected + " " + spelling.suggest(i)[0][0]
        return corrected
