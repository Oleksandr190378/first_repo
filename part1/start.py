from typing import Any

import redis
from redis_lru import RedisLRU

from part1.models import Author, Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag: str) -> list[str | None]:
    print(f"Find by {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result


@cache
def find_by_tags(tag: str) -> list[str | None]:
    tags = tag.split(',')
    print(f"Find by {tags}")
    result = []
    for tag2 in tags:
        quotes = Quote.objects(tags__iregex=tag2)
        res = [q.quote for q in quotes]
        result.extend(res)
    return result


@cache
def find_by_author(author: str) -> list[list[Any]]:
    print(f"Find by {author}")
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        result[a.fullname] = [q.quote for q in quotes]
    return result


def main():
    while True:
        i = input('Enter command and value:  ')
        com = i.split(':', 1)
        match com[0]:
            case 'author':
                res = find_by_author(com[1])
                print(res)
            case 'tag':
                res = find_by_tag(com[1])
                print(res)
            case 'tags':
                res = find_by_tags(com[1])
                print(res)
            case 'exit':
                break
            case _:
                print("Unknown command")


if __name__ == '__main__':
    main()
