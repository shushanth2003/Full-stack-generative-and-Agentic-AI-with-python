class MakeaArray:
    @staticmethod
    def make_a_class_array(text):
        lists=[items.strip() for items in text.split(",")];
        return lists;
text="book  ,  is  , not   , myself";
makearray=MakeaArray.make_a_class_array(text);
print(makearray);
