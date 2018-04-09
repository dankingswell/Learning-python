from bs4 import BeautifulSoup as bs


html = """
<html>
<head></head>
<body>
    <p class="first" data="scrape me"> yummy yummy soup </p>
    <spann data="data"> look in here </spann>
    <p>just another p</span>
    <div>
        <p> hiding in a div </p>
    </div>
    <ul>
        <li> first li</li>
    </ul>
</body>
</html>
"""
soup = bs(html,"html.parser")
print (soup.find("spann"))
print (soup.find_all("p"))
print (soup.body)
print(soup.find(class_="first"))
# class is keyword so need name_
print(soup.find(attrs={"data" : "data"}))
# must use KVP

## methods searched use .find can me indexed[data]

print(f" indexxxx {soup.find('p')['data']}")

## CSS Selectors
# .select returns a list
a = f"CSS selection {soup.select('.first')}"
attr =  f"attr select {soup.select('[data]')}"
print(a)
print(attr)



## extracting data from pages
#get_text inner text
# name tag name
# attrs attributes 


## getting inner text
b = soup.select(".first")[0]
print(b.get_text())
print(b.name)
print(b.attrs)

### NAVIGATION
# will give a list with \n's
contents  = soup.body.contents[1]
# gives descendant
siblings = soup.body.contents[1].next_sibling.next_sibling
print (siblings)
# finding parents
find_parent = soup.li
print(find_parent.parent)

## find next sibling skips new lines
siblingss = soup.body.contents[1].find_next_sibling()
## a string can be passed to find next to specifiy what you want to look for
# such as a class
print(siblingss)
