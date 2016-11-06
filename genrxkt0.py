import fontforge
import subprocess
import urllib

# Create new font TypographyKT.
newfont = fontforge.font()
newfont.fontname="TypographyKT"
newfont.save("TypographyKT.sfd")

font = fontforge.open("TypographyKT.sfd")

# Get Char_List.txt
charlist = urllib.urlopen("https://raw.githubusercontent.com/chen17/rxkt0/master/Char_List.txt").readlines()

for i in range(len(charlist)):
  url = 'http://taiwancamping.club/RX/kt0_bw/' + charlist[i].split()[0]
  char = int(charlist[i].split()[2])
  charjpg = charlist[i].split()[2] + '.jpg'
  charbmp = charlist[i].split()[2] + '.bmp'
  charsvg = charlist[i].split()[2] + '.svg'

  print 'Working on ' + charlist[i].split()[3]

  # Get jpg file.
  urllib.urlretrieve(url, charjpg)

  # Convert into bmp.
  subprocess.check_call(['/usr/bin/convert', charjpg, charbmp]) 

  # Convert into svg.
  subprocess.check_call(['/usr/bin/potrace', '-s', charbmp]) 

  # Paste svg into fonts.
  glyph = font.createChar(char) 
  glyph.importOutlines(charsvg) 

  # Remove process files.
  subprocess.check_call(['rm', charjpg, charbmp, charsvg])

font.generate("TypographyKT.ttf")
