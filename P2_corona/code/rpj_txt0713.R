library(KoNLP) # 한글 자연어 분석 패키지
library(dplyr) # 데이터 처리에 특화된 패키지
library(stringr) # 문자열 데이터 가공을 위해 사용하는 패키지

useSejongDic()

txt <- readLines("d:\\data\\R_pj\\acrl1.csv", encoding="UTF-8")

txt<-str_replace_all(txt,"\\W"," ")
txt<-gsub("\\d+","",txt)
txt<-gsub("\\n+","",txt)
txt<-gsub("[A-z]","",txt)
txt<-gsub("[[:cntrl:]]","",txt)
nouns <- extractNoun(txt)

#추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도표 생성
wordcount<-table(unlist(nouns))

# 데이터 프레임으로 변환
re_word <- as.data.frame(wordcount, stringsAsFactors = F)

#변수명 수정
re_word<-rename(re_word,word=Var1,freq=Freq)

#두 글자 이상 단어 추출
re_word<-filter(re_word,nchar(word)>=2)

#빈도수가 많은 순
top_20<-re_word %>%
  arrange(desc(freq)) %>%
  head(1000)
top_20

write.csv(top_20,'d:\\data\\R_pj\\testcsv.csv')
#write.table(top_20,paste0('d:\\data\\R_pj\\txtacrl',as.character(i),'.txt'))  