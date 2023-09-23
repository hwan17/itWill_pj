library(KoNLP)
library(dplyr)
library(stringr)
library(RColorBrewer)
library(wordcloud)

useSejongDic()

setwd("d:\\data\\R_pj")
#txt <- readLines('crl1.csv',encoding = 'euc-kr')
#txt <- readLines("d:\\data\\testcrl.txt")

for (i in 6:6){
  #print(guess_encoding(paste0('d:\\data\\R_pj\\acrl',as.character(i),'.csv')))
  
  txt <- readLines(paste0("d:\\data\\R_pj\\acrl",as.character(i),".csv"), encoding="UTF-8")
  #txt <- readLines("d:\\data\\R_pj\\acrl2.csv", encoding="UTF-8")
  #View(txt)
  head(txt)
  
  
  txt<-str_replace_all(txt,"\\W"," ")
  
  txt<-gsub("\\d+","",txt)
  txt<-gsub("\\n+","",txt)
  txt<-gsub("[A-Za-z]","",txt)
  txt<-gsub("[[:cntrl:]]","",txt)
  #txt<-gsub("관람객","",txt)
  nouns <- extractNoun(txt)
  #추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도표 생성
  wordcount<-table(unlist(nouns))
  
  # 데이터 프레임으로 변환
  re_word <- as.data.frame(wordcount, stringsAsFactors = F)
  
  #변수명 수정
  re_word<-rename(re_word,word=Var1,freq=Freq)
  
  #두 글자 이상 단어 추출
  re_word<-filter(re_word,nchar(word)>=2)
  
  #빈도수가 많은 순으로 20개만 
  top_20<-re_word %>%
    arrange(desc(freq)) %>%
    head(1000000)
  top_20
  
  #write.csv(top_20,paste0('d:\\data\\R_pj\\nccsvacrl',as.character(i),'.csv'))
  write.csv(top_20,paste0('d:\\data\\R_pj\\csvacrl',as.character(i),'.csv'))
  #write.csv(top_20,'d:\\data\\R_pj\\testcsv2.csv')
#write.table(top_20,paste0('d:\\data\\R_pj\\txtacrl',as.character(i),'.txt'))  
}
