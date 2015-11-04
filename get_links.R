rm(list=ls())
library(tm)
library(rJava)
library(tm.plugin.webmining)
library(SnowballC)
library(XML)
library(RCurl)
library(httr)
library(wordcloud)
library(rjson)
library(RCurl)
library(plyr)
library(rmongodb)
library(ggplot2)
library(rvest)



mongo <- mongo.create(host = "127.0.0.1", name = "", username = "",password = "", db = "Medias")
mongo

mongo.is.connected(mongo)

clean<-function(link,lien){
  
  link<-subset(link,substr(link,1,nchar(lien))==lien)
  link<-subset(link,substr(link,nchar(lien),nchar(lien)+3)!="/tag")
  link<-subset(link,substr(link,nchar(lien),nchar(lien)+3)!="/rss")
  link<-subset(link,substr(link,nchar(lien),nchar(lien)+4)!="/feed")
  link<-subset(link,substr(link,nchar(lien),nchar(lien)+10)!="/wp-content")
  
  return(link)
}

aspirateur_liens<-function(lien,balise){
  links<-NULL
  lego_movie <- try(html(lien),silent=T)
  if (class(lego_movie)!="try-error"){
    hi<-html_nodes(lego_movie,balise) 
    links<-html_attr(hi,"href")
    links<-unique(links)
    a<-which(substr(links,1,1)=="/")
    for (i in (1:length(a))){
      links[a[i]]<-paste(substr(lien,1,nchar(lien)-1),links[a[i]],sep="")
    }
    
    links<-clean(links,lien)
    
    for (i in 2:length(links)){
      lego_movie <- try(html(links[i]),silent=T)
      if (class(lego_movie)!="try-error"){
        hi<-html_nodes(lego_movie,balise) 
        newlinks<-html_attr(hi,"href")
        newlinks<-clean(newlinks,lien)  
        links<-c(links,newlinks)
        links<-unique(links)
        print(length(links))
        }
    }
    return(links)
}}



liens<-c("http://www.lequipe.fr/","http://www.lemonde.fr/","http://chokomag.com/","http://www.liberation.fr/","https://www.dataiku.com/","http://sublimeskinz.com/")
library(rmongodb)


for (i in (1:length(liens))) {
  
balise<-"a"
links<-0
links<-aspirateur_liens(liens[i],balise)

#On doit maintenant sauver dans mongo dans la table links





if (mongo.is.connected(mongo)==TRUE) #Pour checker si on est bien connectés
  
{

  #On insère la query 
  mongo.insert(mongo,"Medias.links",list(name=liens[i],liste_links=links))
  
}


}









