# moby_dict

Python API for the Moby lexicon project, the largest word list in the world. Further details in the [references](./references)

## How to use

- install:

```bash
pip install moby_dict
```

- usage:
```python
from moby_dict.corpus import word_list
word_list.download()
# Wait some minutes...

words = word_list.single()
print(len(words)) #354984

names = word_list.names()
all_words = word_list.all()
print(len(all_words)) #390370
```


## References

- [Wikipedia on Moby Project](https://en.wikipedia.org/wiki/Moby_Project)
- [Electronic Dictionaries](http://www.clres.com/dict.html)
- [Moby Thesaurus](http://moby-thesaurus.org/)
- A similar project but in Javascript: [words/moby](https://github.com/words/moby)
- [Moby Project (IPFS)](https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Moby_Project.html)