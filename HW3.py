import pickle

class UnigramMorphAnalyzer:

    def train(self):
        p_dict = {}
        p_data = []
        with open('p_data.txt', 'r', encoding="utf-8") as f:
            for line in f:
                for i in range(1, min(len(line.split()[0])+1,5)):
                    p_data.append(line)
        p_statistics = {}

        for token in p_data:
            for i in range(1, min(len(token.split()[0])+1, 5)):
                if token.split()[0][-i:] in p_statistics.keys():
                    p_statistics[token.split()[0][-i:]] += [token.split()[1].strip('/n')]
                else:
                    p_statistics[token.split()[0][-i:]] = [token.split()[1].strip('/n')]

        for i in p_statistics:
            p = {}
            for item in set(p_statistics[i]):
                p[item]  = list(p_statistics[i]).count(item)
                p_dict[i] = p
        return p_dict

    def save(self):
        with open('p_statistics.pickle', 'wb') as f:
            pickle.dump(self.train(), f)

    def load(self):
        with open ('p_statistics.pickle', 'rb') as f:
            return pickle.load(f)

    def predict (self, token):
        p_data = self.load()
        dict = {}
        token = token[-min(len(token), 4):]
        total = sum(p_data[token].values())
        for i in p_data[token]:
            prob = p_data[token][i]/total
            dict[i] = prob
        return dict


