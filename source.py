import sys,time,random,webbrowser
BaGua = ['乾','坤','坎','離','震','巽','艮','兌']
GuaXian = ['天','地','水','火','雷','風','山','澤']
Gua08 = ['☰','☷','☵','☲','☳','☴','☶','☱']
Guadict = {'111':Gua08[0], '000':Gua08[1], '010':Gua08[2], '101':Gua08[3], '001':Gua08[4], '110':Gua08[5], '100':Gua08[6], '011':Gua08[7] }
Gua64 = {'000000':'䷁地地坤',  '100000':'䷖山地剝',  '010000':'䷇水地比',  '110000':'䷓風地觀',  '001000':'䷏雷地豫',  '101000':'䷢火地晉',  '011000':'䷬澤地萃',  '111000':'䷋天地否',
         '000100':'䷎地山謙',  '100100':'䷳山山艮',  '010100':'䷦水山蹇',  '110100':'䷴風山漸',  '001100':'䷽雷山小過','101100':'䷷火山旅',  '011100':'䷞澤山咸',  '111100':'䷠天山遯',
         '000010':'䷆地水師',  '100010':'䷃山水蒙',  '010010':'䷜水水坎',  '110010':'䷺風水渙',  '001010':'䷧雷水解',  '101010':'䷿火水未濟','011010':'䷮澤水困',  '111010':'䷅天水訟',
         '000110':'䷭地風升',  '100110':'䷑山風蠱',  '010110':'䷯水風井',  '110110':'䷸風風巽',  '001110':'䷟雷風恆',  '101110':'䷱火風鼎',  '011110':'䷛澤風大過','111110':'䷫天風姤',
         '000001':'䷗地雷復',  '100001':'䷚山雷頤',  '010001':'䷂水雷屯',  '110001':'䷩風雷益',  '001001':'䷲雷雷震',  '101001':'䷔火雷噬嗑','011001':'䷐澤雷隨',  '111001':'䷘天雷无妄',
         '000101':'䷣地火明夷','100101':'䷕山火賁',  '010101':'䷾水火既濟','110101':'䷤風火家人','001101':'䷶雷火豐',  '101101':'䷝火火離',  '011101':'䷰澤火革',  '111101':'䷌天火同人',
         '000011':'䷒地澤臨',  '100011':'䷨山澤損',  '010011':'䷻水澤節',  '110011':'䷼風澤中孚','001011':'䷵雷澤歸妹','101011':'䷥火澤睽',  '011011':'䷹澤澤兌',  '111011':'䷉天澤履',
         '000111':'䷊地天泰',  '100111':'䷙山天大畜','010111':'䷄水天需',  '110111':'䷈風天小畜','001111':'䷡雷天大壯','101111':'䷍火天大有','011111':'䷪澤天夬',  '111111':'䷀天天乾'
         }
print('假爾泰筮有常，OOO今以某事，未知可否。爰質所疑於神之靈，吉凶、得失、悔吝、憂虞，惟爾有神，尚明告知。')
yao=''
yao2=''
buyao=''
  
for i in range(6) :
      print('請卜第'+str(i+1)+'個爻:')  #模擬擲三枚硬幣
      keystock=input()
      res01=random.randint(0,1)
      res02=random.randint(0,1)
      res03=random.randint(0,1)
      res=str(res01)+str(res02)+str(res03)      
      if  res == '111':      #處理爻變； 產生變(之)卦
            sign='—'
            buyao='1'
            sign_var='+'
            sign2='- -'
            buyao2='0'
      elif res == '011' or res == '101' or res == '110' :
            sign='—'
            buyao='1'
            sign_var=' '
            sign2='—'
            buyao2='1'
      elif res == '000' :    #處理爻變 ； 產生變(之)卦 
            sign='- -'
            buyao='0'
            sign_var='+'
            sign2='—'
            buyao2='1'
      elif res == '100' or res =='010' or res == '001' :
            sign='- -'
            buyao='0'
            sign_var=' '
            sign2='- -'
            buyao2='0'   
      print('第'+str(i+1)+'個爻是'+buyao+sign+'    '+sign_var)      
      yao = buyao + yao
      yao2 = buyao2+yao2
      
result_o=str(Gua64.get(yao,0))
result_v=str(Gua64.get(yao2,0))
print('主卦是: '+result_o+'     之卦是: '+result_v)    #印出結果
webbrowser.open('http://zh.wikisource.org/wiki/周易/'+result_o[3:9].rstrip())      #從維基百科查詢正卦解釋
webbrowser.open('http://zh.wikisource.org/wiki/周易/'+result_v[3:9].rstrip())      #從維基百科查詢之卦解釋 
