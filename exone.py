#added smth
import string

def both_ends(s):
	if len(s)<=2:
		return 
	else:
		return s[0:2]+s[-2:]

def fix_start(s):
	return s[0]+string.replace(s[1:],s[0],'*')

def MixUp(a,b):
	return b[0:2]+a[2:]+' '+a[0:2]+b[2:] 

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

print 'both_ends'
test(both_ends('spring'), 'spng')
test(both_ends('Hello'), 'Helo')
test(both_ends('a'), '')
test(both_ends('xyz'), 'xyyz')

  
print 'fix_start'
test(fix_start('babble'), 'ba**le')
test(fix_start('aardvark'), 'a*rdv*rk')
test(fix_start('google'), 'goo*le')
test(fix_start('donut'), 'donut')

print 'mix_up'
test(MixUp('mix', 'pod'), 'pox mid')
test(MixUp('dog', 'dinner'), 'dig donner')
test(MixUp('gnash', 'sport'), 'spash gnort')
test(MixUp('pezzy', 'firm'), 'fizzy perm')


