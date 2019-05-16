
import numpy
import zlib

msg1 = 'x\x9ceQ\xc1\x11\xc3 \x0c\xfb3\x85\x7f\xa5\x8f\x9e\xb7\xc9\x8b;-\xe2\xe1+\t\x08\xbd\x14\x08\x11\x8e"[\xa6\x05\x10\x1e~/\xfc;Z\x0cN\x8e\x8c\x04*\x8aD\xe8\xf1\x1fB-D\xc9AB|\xf0\xe6\x0e.\xc6^\xfc\xe0\x10\x19\x18H/j\x10k!\t}@\xb5\x90\xb2\xe5\x8c|\x9a\xc7\xbb\x8e\x8a-,T\x94\x9f\xea\x87\x11[X\xe9$\xbe\xd4\xb7\x8c4\xf8\x7fbL`\xcb\xb2go\x8f,e\xcf\xa5\xc0\x88K\x04\xd4d\xa0\x92\xb5\x0f\xce\x92\x12\xc3Nv\xeaH\x05\xb4-!\xd5\xec\xde\x9d\x9eB\xb1\xceX\xa7\x81\x95\xb3\x8e\x88\xb2`\xb6\xcb\x86fG\x80~\xdbm\xffW\xf5\xbc\xb9/\xf0\xa1r\xb0'

msg2 = "x\x9cm\x901\x0e\xc30\x0c\x03\xf7\xbcB[\x13\xa0\x85\x7f\x93\xc9\xc0\xf5!z|I\xc9\xf5P\xd4\xb0\x1d\x11\x94I1G\x04\xb5\xff\xac#2R\x1b\x82>\xb8\xd1eq*F\xf0\x8e\x19\xb7\x8a\x17W\xc3\x14G&\x13\x9e\xe4d\xa8 \xa3\xe1Q\x02[\xd0h\x0b\x8b\x93\x80Z\x91\xa4\xbfC\x1a\xee\xc8\x9e\xe5DW\xf5\xa4\xaf\x98Y\xd8\xef\xca\x82\xf2d0\x84'_\xce\xe3\x9e\\6t\x98uV\xbe\x87Uzl\xd76cq\xce\xd0)v\x1e\xc9\xb4f\xaf\xb4\xdb\xcf?\xfb\x00\x9f\x1fT\xda"

msg3 = 'x\x9cu\x8f\xc1\x0e\xc30\x08C\xef|\x85oM\xa4N\xfc\xcdN\x91\xbc\x0f\xe1\xe3g\xd3d\xb7\xa5j\x03\x18\x1en\x80\x04\x9eO\x9f_\x00\x04\x96\x9eDJU\x99\x03\xd3\x01\xdd\x1c\x90\xf4\x96H\xddU\xa8,\\L\xbc8\xad\xa1XK\x8d\xb9x\xb3\x9c\xc1iYc\x17\xc8\xc1\xf9p\xb9\x97\x86q\x9f\xc3\xc4\x85\xd5ym/\x14\xaa\x99\x14\xae\x1c\xdeGC\x9b:/\x1a\xff\xb8\x96\x96\xbd\xd1L\xdf\xa9A\xf7\xcbCh|\xb0\x19\xe9B/V\xddv\xfd\x7f6\xcc\xda;S\xf9\xa2\x07f\xe0\xff\xf9\x02K`Q\xe6'

msg4 = 'x\x9c}\x90Q\x0e\x82!\x0c\x83\xdf9E\xdf\x90D\xe5B$\xf5 ;\xbc]\x19>\xf8\x1bY\xd6@\xc6\xbeQ\x1a@\x12\xbfWCH\x17\x98\xc1\xcc\xda\x9eb\x0cI\xe7\xc4\x83\x03|\xe5!\xef\xbb\xa8\x86\x19\x0c,m\x94w\xc6\x8e\xea$o\x1c,\\\xe1\x15.v\n2\x13X\x92\xf8\xae\xd6\xc4>\xc55\x10G\x92*X;Vj\xb4\xe4jE@?\xf0\xe2\xd3VD\xf1\xbd\xaf"k\xa4\x14\xf5\x11;\xddI\x0c\x9d\x04fXvj\xca.\xae0\xf8\x08#\x07\xcc\x0f\xd6\x9f\xc3\xd86l\x85\xd9\xf9g\xb57\xa2\xe2h\x95'


msg5 = 'x\x9c\x9dRA\x8e\xc3@\x08\xbb\xe7\x15\xdc\xba\x91\xda\xf0\x81}\xc7\x9e\x90\xdc\x87\xf0\xf8\xc5\x86DUv[Ue\xa2\x0cC\x0c\x98q\x163\xd0\x0cV\xa6\xd7;6\xc0\xc5\x92\x1e\x92\xfb\x17V\x95Q1\x96\x1co?\x19\xe6,t\xedK\xc5R\xebb1\x9b\x1b\xeeU\xe9\xf6m\xf2*\x06\xb7\x1bV\x1e-v`\xd6\xb3\xb0\xaf:gB+\x11\xc0\xd5\x1cpy\xfa\\\xce\xbc}\x80Q\x98\xcan\xba"\xd2\\\xeb\x1bA\x15\xaf\x9a*\x8c\x7f\xee\xa3\xa2\xce\xb9E\x97l.\x10k\x91&\xef\x8e\x98X\xf7\xbcg\xe3\xad\xcd\xb2\xad\xca5\xb9~\x12\xdb\xd0/"\x84\xac\x7f\xb3U\x12=\xfd\x88\x87\xa3\xcf\xa1&\xc6\x95\x0c\x8f\xbdgE\xee\xe2A\x02\xf6p\xa3&\xcf@h\x0e?e\x0b\xbc\xdd\xa7\xcc\xa8\xd1=:\x04J\xccK\xb7\x9f\xc7d2\xd7\xa8\xd2 G\xbc\xbev\xb4s\xa8\xd9\xf7\x9f\xa7\xb9K\xda`\xe9\xaa,\x80f\xd0\x8f1\xbc\x9f[e\x0bH\x8c\x0b:3H\xee\x19\xffE\xb6\x97\xea\x01\xd2\x8e\x9d\\\xf0\xe1\xdf\x90/;7\xf3\xcf\xed\x17M$\xdc\xd5'


msg6 = 'x\x9c]\x90Q\n\x800\x0cC\xffw\x8a\xfc\xa9 \xecB\x83x\x90\x1e\xde\xa4V\xd9\xac\xa3\r]\x16\x1e6\x80>j.~m\xad\x86@\x04v\x1e\x94W\x9a\xc8\xf6\xf3\xdaF_u\xf0\xd2\xd80\xe2y\x19?\x1bC\x87\x83<_\x1d\xc3z\xb5)\xcch\xa1\xd1k)giNi\xc9\x94>\xbf\x01\x0b\xb4\xf6oZ\x91\x08\x0e\xa3\x085J9D_\xcb\x94\x82c/B\r+m\xf7\xbc;\xda\xfa\x7ff\xc2\xb9n\x9eqS]'


msg7 = 'x\x9c}NA\x0e\x800\x0c\xba\xef\x15\x1c5\xd1\xf4\x03>\xa5\t>\xa4\x8f\x17:o.\x92\xac\x90A\xd9\x06@\xcec\xbc\xd4\xaa\xf5@\x01\x19@)\xc22\xd1\xe1\x8d\xbb\xf4\xf4+\xa3\x10\xe0\rS\xe0\xb4\xe7=\xe5\xe5kj$y\xd0$\xd1=\x95l\x1f\xee\x9bw\xf8b\xe8\xa5\xf3R9\x92k?\xc8p\xa7\x7f\xb4\xf2\xff\xf1\x00\xd4_6r'

msg8 = 'x\x9c\x85SA\x92\xc4 \x08\xbc\xfb\nn\xc9T\xed\xac\x1f\xd8w\xec\xc9\xaa\x9e\x87\xf0\xf8\x85\x06\x135I\xadc\x1cA\x94\xa6\x81"\x02\xc0\x17\x99\xc6"\x1e\xa3\x88B\xa0\xd5>\xbf\xc3ic\x97\x97\xed\xe2\xa9\xc5^TT\xc5\xed\x9b\xfc\x8a\xcd*o\xbc\xaa\xca\x06\xee\xae\xef\x03j\xd6v\xa5\xa1r\x9aB\\\x15\xbb\xf5}\xa4\xe7\x1d\xc4\x10\xb2{\xbd\xc7c\xd0?\xbe\x18\x1c\xc3 \x8d\xb2Y\xdb\xc5\xd0.\xf6\xe6\xf4\x8b\x9e\xab\xc3RP6k\xfb\xa7\xf6\x0e\xff\xa8\\\xe5\x99\xe2B\xa0\xc8,HD\xca\x80\x98\x92\x0c\x08q\x90\xf6\x1b\x1c\xb5S\xd7c\xf90\x14i\x19\x90\x1f\xb9\x0e\x81\xe7\x1bI"\xb1\xc7\xa2\xfdGe\xe8,\x89\x1d\x0faxR\xcd\xf5\x04p\x1cV\x05\xb4\xcf4ZU\xecx\xffL\x00/\xc3\xf1\x10Ks\x1f\xd5\xa9\x19\x00\x06\'\xa3\xa3\xf2?\'^\x8b\xc8\xf3!\xbf\x0f\x9c\x0c\x89\xde\xec~\xe4\xf7\x99\x93\xb3\xf0*\x82\xff)}\xcb\xee.\xde\xec\x12\xd6\xe3\xb2\xcb\xe6\x99\xed\x8f.9ksm\x9e\xc9^\xa2K\x8e\xdaLjel\x9e\x99\xcfl\xd4\xc4\x12h\xa4\xf7\xd1\xd2\xc5Qo\x13}\xecg=(\x8eC\x9c\xf6\xc9\xd7Iic\xc3t\x99\x87{\x0f\xa2\xc8u\xe8C\xc3\xb8\xf9\x1f\x9fE\x1a5'

msg9 = 'x\x9c\x85\xcc\xc1\r\xc00\x08C\xd1{\xa6\xf01\xbd\x94\x85\x90~\x07a\xf8\x823@\x10HO\x96\xc5\x92\x00!o\xcb8\x99\xf3\xa5j\x95\xb2Ta\x05\xa9\xa3\xb9r\xa1J\xef\xd7\xd8\xb8\xa5\xb4&g\n\xfd\xaa\x91\xb3\x10\x84\x92t\x06\x9bg\xe92?z%*X'

msg10 = 'x\x9cm\x91\xd1\x8d\x031\x08D\xff]\xc5\xfc\xed\xae\x94\x1c\r\\\x1d\xf7eiR\x08\xc5g\x06;\xeb\xdb$FB\x184\xf0\x8c\x1b@\x12\xc4\xe5\xf0\x9f\x7f\xaf\xe94\xa4$;\x0e\xf9\xaa\xba\xc3\xce\xe3\xf4P\xedS\x84Df$6\xa0\x03\x01>\x94\xe9\xf8S\xe8d\xcf\xf8:\x89\x94\x8ee\xe8\xe4\xcd\x97\xce\xa8\x84s\x1f\x94\xad\x06\x95\x126\x07\xe1&2M\xadv\xf5l\xbf\x80\\"\xc5\x81;\x0fl\xcc\x17\x9fMS\xc5)\xc2\xaa\xc6\xce\xfb\xef\xc2\x13C7c\x91\x98o\xa2\xce\xa9\xb3\x8a\xd0mp\xb6\xb1/\xf0E\x02\x0c\xac\x89;\xd3k\xa7fh\x83G\xce\xbb\xa3e\x89\xdd=\x8br\x1b\xe9\x93\xd9\xdb\xa4D\xb5/\x03D\xaf\xe7\x16!\x07%~Fz1\xa7\x07\x8e\x95\x9f_q\xfd\x94\xb5\xef\xeby\x02\xa4\xe8\x8e}'


msg11 = "x\x9c\x85PA\x0e\xc20\x0c\xbb\xe7\x15\xbem\x93\x18\xfd\x00\xef\xe0T\xc9<$\x8f'N\x8aZ\xa1!\\m\xcd2\xb7vl\x00\x81\xf1\x1aX\xeb\x0f\x0c\x1e\x0b;\x0f\x82\x02\xaa\xa1\x0fh!\xf7\xe2\x91\x8e\x8e'\x1aN\x1e\xd5h\xf1\xb3cC\x8f\xe2\x15-S3x\xf4\xce\xd6UUCe\xa3\xbb\x8a[\xf20\x04R\xa24W\xe8T\x93\xee\xb8xJ\\\xc2\xa0\x8b\xa5[\x12\xfc\xc9\xcb\xc9\xfeB\xf3\xc6di\x90\x15\x8d\x0c\xcfX\x16\x1e\xc2\xe8\x96I\xec<\x1fQ\xca\xaa\x12\xda\xa6\x0b\xe5\xe2\xf9T\x12A\xbfs$\xb4z\xb5o#~=\x89\xbd\x01\x9e\xd6h\x94"


msg12 = 'x\x9c\x8dO\xc1\r\x03!\x0c\xfb3\x85\x7f=\xa4"\x16\xe8(\'\xb9\x83x\xf8\xda)wB}5@\x94`+v\x1a@\x12+x\xa7\xdfh\x90\x813\\\xf2`\'\x05\xa5\xc6\xf7T\xe5\x17\x1e01(\x8e\x17\x8e$p\x82o\x03\x0f\x9c3\xcd`7\xcf\x8c\xcc\x9b\xb9In|\x9f\xfeV!\x01\xd5JE\x19m\x03\x16E\t\xdb\x01\xb4\x19\xb7\xaeq\x95\x9c\x8a",n\x99\xe9\xdb\x1eK3\x06\xbc\x90\xf5,t\x99\xd16\xef\xaf\xf8\x00%\xbeMQ'

msg13 = 'x\x9c\x95P[\x0e\xc20\x0c\xfb\xef)\xfc\xb7!1r\x01\x8e\x12);H\x0f\x8f\xed\x14i\xc0\x17\x99\xd6\xbc\x9c\xd4\xee\x00\xaa\n\xb6vJW\xe1\xd7\x06\x82\x80)\xd0\xc4$\x8c!\xd2\x91\xc7<\xdc\x91\xfc@2\xc9\xc0Q7"8\xc23\xb0\xa9T\'\xf6:\x9e\xdd\xdbJ\xf1\xe0\xa2\xaaHm\xcf\xbe\xc1\xff,f\xf7\x8aw\x8fU\xc5\x03\x17\xa2\xeb\xe6E\xde\xe7\x97\x0en\x17Q\xcb\xb5\n\x03\xc5I_\xb6\xfb\x84\x8b\xac\xf4Y\xc5\x02\x9a\x13\x1e\xa7\x83+\\(\xd1\x8bV\xd1}\x17\xa6\xe4\xecz\x82+\xfc\x1f{\x01f\xd5b\x96'

msg14 = 'x\x9cuQ[\x0e\xc3 \x0c\xfb\xe7\x14\xfek\x91\xba\xe56\xfbB\xf2E8\xfcb\xf3\xa8:i-\x82`9\xb1\x13\n@/\xac\xfd\xdfW\xd0\xd1s\x91\xd4\x0e\xd2):H\xfe2\x13\t\xbcX3<\x88\xa6\x03h\x86\xa8\xac\xcdd\xefl\xaa\x99U\xdfd\x08\xe1\x80NGu2[\xfe\x81\xc8\xc2\x82O\x8c:\xb7\x8b\xd5FI\x1d|\x92j\xd9\xb4\x1a\xb2\xb0\xcd`\xa2\x83)5IE\xe3\xe5\xb6\xa6\x99\xed\xe2R/b\x92\xc3\xb7{\x97\xd2\x9e\x86\xe53\x08\xa5\x95)|\xa0\xf5IY\xd30\xcc5\x84dZX\xfd\xdb\xc4\xe5\xd2s\x1a\xe1Y\x8c!\xd4\xf2x\x07)=\xae\xfd\xbe|\x01#\xb6th'

msg15 = 'x\x9c}Q[\x0e\xc30\x08\xfb\xcf)\xf8k+\xad\xe3\x02;\xc7\xbe"y\x07\xe1\xf0\xb3I_k\xb3B$\xda\x00\x8e\r\xc5\x0c2\x83m\xa6\xdf\xbfV,\x94Ed\xcc\xd2`\x88\x84\xa0\xe3\xdc^L\x15\xf2\xc1\xaa\xdb\x8cI\r\xce\xdaj\x83b\xbb;5$~\x04*\x84M\xd7\x87\xf3\x961\xef\x920\x96\x06\xb4\x87\xc7\xc4N\xc7J\xee\x98ZH\xb3\xa1\xda\xdbx|-\'\x93\x95\xdc!%\x95$\x9d\x94*\x9c\'\x1a\x19\xc2<\xa1\x0b\x11\xd9S5\xb9*_\x04\x1a\xd6TF>\xfb3\xe2\xceX\t\xf3\xb0T\xc9\x0f\xf2\xd5C\xd3m\x03E\xba\xdd\xa2\x9e\xf7\xe0\xa8\xd6\xc8\xe4\x9a\x16R\x97\x95m\r\xc9?\xf6\x91\xe0\xd3t\x8d\x98_\xd7\x8eB|\xa7\x84\xaaIx\x1e*\t\xe9r\xe4\x06:\x94:\xd6t\xf5\xec\x0b\x1b\x98\x97\xe2'

msg16 = 'x\x9c\x8dO1\x12\x830\x0c\xdby\x856`h\xf3\x1b\xa6\xdc\xa9\x0f\xf1\xe3+9\xa6%e\xa9\x0el+Q,{\x01\x98\xdf\r\xfcdU\x0b\x02=\x104P\xd1\x17>3\x0fW){\xbe\xd0\xf0\xe0\x8e\xa3\xf2\x9a\x97\xe0`%ctv\xbf\xebl\x99%\x12T\x16\xa3e\xf6\xf0x,\xa7t\x1b\xf4\x0b\x9b\xaezz\xf6\x07\xcd\x8bN\xb2\xec\x9b\xfd\xe1$v\xd2\xabLc\xd3\xcb\xa2\x82\xe8\xd8\xe0\xd7t\x1b\xebTP#\xfd7\x99\xcf\xd9b\n\xdb4\xd8\x90\xfd\x837\x06\x8eb\xc8'

msg17 = 'x\x9c\x8d\x92\xd1\r\x830\x0cD\xff3\x85\xffZ$P\x16\xe8(\x96\xae\x83x\xf8\x9e\xcfA\xb4P\x01A$!:\xfb\x9e\x1d\x9a\x19\x00\xbb5\x9a\x05g\xbf\x15\x90\xda\x98\xac\x1b\xcc\xaf\xd4\xd42ewNOLW\xda=\xf0!;\xbe\xb4\xf2\xe7\x0b\x85\x85\x8c$\x81\xd2\xe4\xc1\xc6\x9b\xe6a\x0f\x9e2\xec=by`^[C\xa9\x997Y{@\xfd\x00f\xe8\x9b\xc9"j\xebk)M>\xc0\x11\xf3H\xde\x8afPU\x10\xaaZ&\xd3\xba\x82\xab\x0f\xa1Gx\x0b\xcd\x1e\xa85\x0bY^\x1b\xb8\xb8c\x83\xcb\x0f\x1f\xc5\xf7_l\xdd\xda\xb0\xfd\xd3\xd9=\xadX\xb3_\x11\xfa5\xcen\xcd\xcb\x98\xeb|\xa9]G$\xdd\xd9\xf8\x00\xc9\xd9\x8dD'

msg18 = 'x\x9c}OA\x0e\xc30\x08\xbb\xf7\x15\xbeu\x95\xba\xf1\xa1H\xdeCx\xfcl\xc8&uSF\x02Q\xc0\x06\xbc\x01$\xf1kN~\n\x9c^\xb6!\xf59\x8a\xe7\x0b60\x81\x11z\xaa_\xf6\x99\xa5\xa6\xa8z\xa7xO\xfdv\x81\x0b5"\xd1y\xc3M\xda\x85\xa4)j\x14CA~2\xfb\x14F\xc1y\x0f4&\xf1 o8\xb6\xab\x96\xcb\xd2_\xd6]BS\x02nTRfw/\xbdf\x8a\xa2\xa1\xd6\xc2\xb0&!\xb3<\xbd\xfb\x8a\xf2\xd62\xe6\x9b\xed\xe7\x1f\xcaboM]\xd8\x0b|dd\x88'

msg19 = 'x\x9c\x85\x91Q\x0e\x84 \x0cD\xff9E\xff\\\x13\r\x17\xd8\xa34\x99=H\x0f\xbf\xedP\x12\xc0\x041"\xe2\xb4\xbc\x19\x8b\x08\x00y\x1fE\xccg}W\x87\xd0N\xa9\x02\xd1\xad\xd4\x85\xde\xac\xaaO\x1f\x9c[\xe1\n\xf9\xe8\x8b.\xe4\xb1~\x835\xc6#\xf8\x1d\xec\x11\x1b\xc9\x18g\x9a\x1c\xbe\xe55\xbf,\xf4\r\xd1\xb6\x14\xb8\xd4;\x06_5\xd0=p\x81\xef\xde\xc6\xac-\x95\xf8\x85\xed\x81\'\xdaB[\x1aA\x92\xb4\n4{\xdef\xb0\x19\xae\x8d\x17\x91n\xc7=\xd0\x9e\x01\x7f\x7f\'!\xfb%R\xbch\x9a\xad\x01;\x087\x19N\x81\xf7\xc0\xc8\x90\x8c\xcf\x9a2\x06ft\x15\x81Z\xc6<\xbb\xee\x811G\x06\xaa\xb8d\xf9\xf53c\x1f6\xb8\xc8\xf1\x07\x01\xd1\x8c\xe7'

msg20 = "x\x9cu\x91Q\x0e\x830\x0cC\xff{\n\xff\x01\x12,\x17\xd89\xf6U\xc9;H\x0f\xbf\xd8)\x9b\x98\xb6\x80\x9a\xa6n\xd3gh\x00\x15 \xbe\x82\x7f\xe6\x9fh\x18\x128\x9c\xab\t\x95Wl\xaa\xa0\x15\x8b\xf4r\xe9\xb5\xa5\xe5\xc1\xe1gA\x0f\x1c\xdc\xb0\xd09V\x1ew\x04\xf8L\xb1\xe3\x81|g5\x06$\xfa\xac\x1b\x8f\xc1\x9e\xcdT8#\x98Mr\xbak\xad3\xfc\xaa\xea\xdc-\xb6\xa2\xf2\xe5\t\xca\xad\xa8&x\x01\xea:+f\xf7\xc6(\xbf'G\xb2&\x9a\xab9\x94\x01I\xb2l\x0biL`\xe7\xb7*\x8elv\xcbv\xc2\xdeq\x0e\xac}\xe5I\x942\x96\x04\xef\xb3\xd7H\x1e\x86\x87\x9f\xbf\xe5\x12/\x17Xt?"

msgs = [msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9, msg10, msg11, msg12, msg13, msg14, msg15, msg16, msg17, msg18, msg19, msg20]


msg = msgs[numpy.random.randint(len(msgs))]

msg = zlib.decompress(msg)

print(msg)
