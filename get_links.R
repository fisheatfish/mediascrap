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
library(XML)

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
  #lego_movie <- try(read_html(lien),silent=T)
  
  lego_movie <- try(read_html(lien),silent=T)
  if (class(lego_movie)!="try-error"){
    hi<-lego_movie %>% html_nodes(balise) 
    links<-hi %>% html_attr("href")
    links<-unique(links)
    a<-which(substr(links,1,1)=="/")
    for (i in (1:length(a))){
      #links[a[i]]<-paste(substr(lien,1,nchar(lien)-1),links[a[i]],sep="")
      links[a[i]]<-paste(lien,links[a[i]],sep="")
    }
    
    links<-clean(links,lien)
    
    for (i in 2:length(links)){
      print(i)
      lego_movie <- try(read_html(links[i]),silent=T)
      if (class(lego_movie)!="try-error"){
        hi<-html_nodes(lego_movie,balise) 
        newlinks<-html_attr(hi,"href")
        newlinks<-clean(newlinks,lien)  
        links<-c(links,newlinks)
        links<-unique(links)
        }
    }
    return(links)
}}

liens<-c("http://www.lequipe.fr/","http://www.lemonde.fr/",
         "http://www.lefigaro.fr/","http://www.tf1.fr/",
         "http://www.20minutes.fr/","http://www.01net.com/",
         "http://www.leparisien.fr/","http://www.liberation.fr/",
         "http://www.lexpress.fr/","http://www.huffingtonpost.fr/",
         "http://tempsreel.nouvelobs.com/","http://rue89.nouvelobs.com/",
         "http://www.lepoint.fr/","http://www.france2.fr/",
         "http://www.europe1.fr/","http://www.ouest-france.fr/",
         "http://www.france3.fr/","http://www.ladepeche.fr/",
         "http://www.lesechos.fr/","http://www.m6.fr/",
         "http://rmc.bfmtv.com/","http://www.slate.fr/",
         "http://www.letelegramme.fr/","http://www.francesoir.fr/",
         "http://www.sudouest.fr/","http://www.rtl.fr/",
         "http://www.radiofrance.fr/","http://www.france5.fr/",
         "http://www.maville.com/","http://www.lavoixdunord.fr/"
         )
library(rmongodb)

library(rmongodb)


for (i in (1:length(liens))) {
  print(i)
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









