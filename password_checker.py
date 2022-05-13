import requests
import hashlib


def reuqest_api_data(query_car):
    url="https://api.pwnedpasswords.com/range/" + query_car
    res=requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res

def get_leaks_count(hashes,hash_to_check):
    my_tuple=(line.split(":") for line in hashes.text.splitlines())
    for h,count in my_tuple:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    coded_pass=password.encode("utf-8")
    hashed_pas=hashlib.sha1(coded_pass).hexdigest().upper()
    first5, tail =hashed_pas[:5],hashed_pas[5:]
    response = reuqest_api_data(first5)
    return get_leaks_count(response,tail)

def main(passw):
    print(pwned_api_check(passw))

if __name__=="__main__":
    main("password")