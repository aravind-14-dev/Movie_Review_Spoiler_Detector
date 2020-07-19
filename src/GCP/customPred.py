import pickle
import numpy as np

class CustomPredictor(object):

    def __init__(self, model):
        self.model = model

    def predict(self, instances, **kwargs):
        results = []
        for instance in instances:
            inputs = np.asarray(instance)
            pred = self.model.predict(inputs)

            #output = ["Spoiler" if i else "No Spoiler" for i in pred]
            results.append({"instance": instance, "prediction": str(pred)})
        return results

    @classmethod
    def from_path(cls,model_dir = "gs://fin_proejct/NB_new"):
        model = pickle.load(open(model_dir+'/model.pkl','rb'))
        return cls(model)
