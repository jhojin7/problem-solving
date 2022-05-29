"""
https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/2085316/Python-or-or-Easy-3-Approaches-explained
https://leetcode.com/submissions/detail/709807839/
"""
from numpy import intersect1d
from __solver import *
class Solution:
    
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        for s1,s2 in itertools.combinations(words,2):
            # set intersection
            if not(set(s1) & set(s2)):
                ans = max(ans,len(s1)*len(s2))
        print(ans)
        return ans

    def notmaxProduct(self, words: List[str]) -> int:
        def hasCommon(wordi, wordj):
            seti,setj = set(wordi),set(wordj)
            # seti = set(collections.Counter(wordi).keys())
            # setj = set(collections.Counter(wordj).keys())
            intersection = seti.intersection(setj)
            # print(wordi, wordj, len(intersection))
            if len(intersection) > 0:
                return True
            return False
            
            # for i in range(len(wordi)):
            #     for j in range(len(wordj)):
            #         if wordi[i]==wordj[j]: 
            #             return True
            # return False
        maxprod = 0
        new_words = []
        for word in words:
            new_words.append(collections.Counter(word).keys())
        # print(new_words[0])
        # return 0
        # for wordi,wordj in itertools.permutations(new_words,2):
        #     if not hasCommon(wordi,wordj):
        #         maxprod = max(maxprod, len(wordi) * len(wordj))
        # print(maxprod)
        # return maxprod
        
        for i,j in itertools.permutations(range(len(words)),2):
            # if no common letters
            # print(words[i],words[j])
            wordi = new_words[i]
            wordj = new_words[j]
            if not hasCommon(wordi,wordj):
                # maxprod
                maxprod = max(maxprod, len(words[i]) * len(words[j]))
        print(maxprod)
        return maxprod
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]

words = ["aabeddecddba","eeefafbceedaab","abfdeedfcbf","dacbdfeccdaaed","bbaeae","ecebefefbafeeaeabbda","fb","ffcbcfcbfbeaaf","dcfeaccbcedeaddeead","caebbdae","ffacafabe","cffbbacceebedffcaade","dfbbeacc","fcabefffefeecfdbdecf","dacfbbfbaaadfde","ddebbf","ccaeeaedffbefeabf","cdbaacfddbebccdfcfb","fcdba","abdeeebedde","bcab","fafeafbfc","dedbfd","acdabcbfacadffebeff","beabcfefbdeaafe","faffaeedeacfeacdbbf","fedcabade","fbdfebeabacdea","bccefebccdafebffd","afadcfafcdcfeb","dfabfbbcede","deacfedfbfbcd","beadddeceaaafbacafebe","cc","bdcedccfdecf","effadbcfc","ffedcdffebf","addadfabecdffcccdf","cddfabcabaeecb","daeadacafbdedc","cccaacbc","fcbbececdea","fbefeafcecacddab","decaadeedddfcfcf","ebbdfcddfaadfda","afd","fcfaeaeabecbbcaffcb","eadfffcfcbfecefeadc","ad","eafbbddefe","ecebabdeafcdb","dcfdfebceaeadfd","aabbeecfbdecfeea","fccebeaeffdfbd","dedfddbedf","cfaccbeddcdccaeacdaa","dbfdefea","ddb","bddbcdcdeade","cbfffea","dafbcfcfbdaafaabcf","eccbdfcffed","bdbfdaedeaffa","efbecddafbedbda","eaaaa","edadaafcadfb","babdbceadafdeeffaf","dccffabeafcda","fcbbbddefadbedafaadca","ddcd","faccfddffcededcdecccd","adfdfedcebadfdcfcaa","eadccca","ddcfabcebceddeecfbb","cfe","bfbacceaacedcccdbefc","aeabec","cfef","af","fccbbe","aeeffecddca","aececadc","dfaeddae","efdebbdfcce","adaaecdaffcbeaefccc","eadedb","afeacdabee","faaaffbdfcaadef","fcaeecfbdfdfaa","eacbfdefcbc","cbcfffcbbefdcbcffbdfe","dfabdceafcb","baacaeebedcabcadfe","defeaf","fffaecaaff","ebddcdfacddbddaddeef","bcecf","caaadabebbb","bcaffbebbaccadafef","dbecbfadbaefbc","fceafbf","dffabbdfbcbfc","fffccaad","ccfaffbbfea","bbeafaedbc","fbdfecdadaaecaed","fdce","ceecbbfecbaaeaacbe","ffafcedaaefffa","bbbbfbbbe","fbaebcbafcabcfdac","ebfaabceaebdddeecfb","cd","aecfeecadddcfddfda","cfbcedeeeaeadbea","cbd","cdbcabafbeadfdeccbdc","bdbedfcbf","ddc","dceacefbffbfcbfffd","eedd","fcacffaeabfcdfcecaaaf","cafceebfdbedebaacff","efeabbafeebddd","cddddfdbb","ecdeeed","fdccdcdab","df","aeaeaecddabe","fefaeebaccaecaf","ebacbced","cbdabcbadff","bdddecdebadcfcfed","bcabbfbe","eefcaadebebdfffdacec","daadc","ffa","aadaa","fbfdcbccabbdfecf","febdfaf","bbcabebcfc","fddaeaeafbbdebbf","eabbeeaaafadedeab","aaeebefff","eeadedeedfefce","acdaafceabdbccfddeffc","ccfbdebdacccc","ffacbeabaebdf","acff","bbcfcfbcedfdee","ecdccbfddbfefffafefdf","bcdbeaffbaeedfca","baedcfbffbdb","faafdbfacefeaddfcfc","ddadcaeafaef","eaefeddace","bcbdacadeaeadabdffbef","aaaf","acfbfccfbbcb","dacfebdc","ecba","aafefebbeafbbaaaff","aeaecfaacfcabfddfba","ebdabdffaabafeacc","fdeeae","aeddedd","fccabaffffbfefcaecced","eeabca","dc","ddffdaeeedecafd","ccaeefcfeffadfedaadd","fdcaefaeddbcfdafebf","adabefd","bdfaddbdcdaedfecbde","beaacecebacae","fbaaea","cbaeffddddabbdcffccfc","fbabacacbcbaaebdb","fafbbfceeddddaffdfcaa","dbb","eadbcbceeef","cdffddccbaeef","dcfeebabafddadedbedc","cfcfecebecb","aedabcdccbdbdbb","abbfacfecaebffa","ffedddfdbbfaaee","ff","beeb","fecdefcdedbadde","cae","fdbdebadeadd","eefbeacedaef","bbcdebbffee","bcccbbebafcaeb","aadbcfcedbfbecaee","efbacddcbfffcefbfacbb","dcfbc","cbfa","fffbbfaabfc","cefccaacbccfdbaab","aaebbcecaadccd","babebadacdbbfacdade","ddefdbdeacfedbf","fefccacbcf","fcddcdababbda","afaaeaccf","ecdbeeeecdd","bfaadfcaffbeacdbfefac","cabcddfefabbe","fcccfaebadea","fbcabbbcabccedb","dbbdbbbffecfedfa","fdbdfcfdaebdabebdcafe","eacfcf","faa","caceccdaeaddcbddffdfe","aaddadcfe","bafaafaacbfcfaebeeec","ebdffaddcffb","dfcfbdbaaeceebbf","fbdecbca","ceacdaddfeafcfbf","acecd","ceabccfdbbdbebbedf","adbacefaebbbaedffaff"]
Solution().notmaxProduct(words)