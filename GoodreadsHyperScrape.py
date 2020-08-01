import time
start_time = time.time()


from bs4 import BeautifulSoup as soup
import urllib.request
from urllib.parse import quote
   
def main():


    thebooklist = open(r"C:\Users\Kritant\Desktop\Project Scrape\TheBookList.txt", "r") 
    
    filename = "DataSet.csv"
    f = open(filename, "a", encoding='utf8')
     
    headers = "title, author, rating, rcounts\n"
    f.write(headers)
    
    for line in thebooklist:
     page_html = urllib.request.urlopen("https://www.goodreads.com/search?q="+ quote(str. rstrip(line)) +"&sort=score").read()
     page_soup = soup(page_html, "html.parser")
  
     containers = page_soup.findAll("a",{"class":"bookTitle"})
     
     
     
     for container in containers :
         newpage_html = urllib.request.urlopen("https://www.goodreads.com"+ container["href"] +"&sort=score").read()
         
         newpage_soup = soup(newpage_html, "html.parser")
         
         title = newpage_soup.find("h1",{"id":"bookTitle"}) 
         title = title.text
         title = title.strip()
         
         author = newpage_soup.find("span",{"itemprop":"name"})
         author = author.text
         
         rating = newpage_soup.find("span",{"itemprop":"ratingValue"})
         rating = rating.text
         rating = rating.strip()
         
         rcounts = newpage_soup.find("div",{"id":"bookMeta"})
         rcounts = rcounts.meta["content"]
         
  
         
         
         author = author.replace('ō' , 'o')
         author = author.replace('ō' , 'o')
         
         
         
      
         print("Title :" + title)
         print("Author:"+ author)
         print("Ratings on five :" + rating)
         print("No of Ratings:" + rcounts)
         
     
         f.write(title.replace("," , "|") + "," + author.replace("," , "|") + "," + rating + "," + rcounts + "," + "\n" )
    f.close()
    print("--- %s seconds ---" % (time.time() - start_time))
     
     
main() 
     

 







