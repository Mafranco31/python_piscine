class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        zip_val = zip(coefs, words)
        ret = 0
        for coef, word in zip_val:
            ret += coef * len(word)
        return ret
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        ret = 0
        for i, word in enumerate(words):
            ret += coefs[i] * len(word)
        return ret

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))
    