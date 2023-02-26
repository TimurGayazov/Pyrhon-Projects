from urllib.parse import urlparse

url = 'www.xakep.ru'
domain_name = urlparse(url).netloc
domain_name = domain_name.replace('www.', '', 1)
# domain_name = domain_name.replace('.ru', '', 1)
domain_name = domain_name.replace('.com', '', 1)
domain_name = domain_name.replace('.org', '', 1)

print(domain_name)
