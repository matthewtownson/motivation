
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
'

msgs = [msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9]


msg = msgs[numpy.random.randint(len(msgs))]

msg = zlib.decompress(msg)

print(msg)
