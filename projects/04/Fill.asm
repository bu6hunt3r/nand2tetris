@color // declare color variable
M=0 // by default that's white

(LOOP)
@SCREEN
D=A
@pixels
M=D // pixel address, goes from 16386 to 16386 + 8192

@KBD
D=M
@BLACK
D; JGT // if(keyboard > 0) goto BLACK

@color
M=0 // set to white
@COLOR_SCREEN
0;JMP // jump to subroutine that colors the screen

(BLACK)
@color
M=-1 // set to black (2's complement 1111111111111111)

(COLOR_SCREEN)
@color
D=M
@pixels
A=M  // VERY IMPORTANT! indirect address
M=D  // color M[pixels] with @color

@pixels
M=M+1
D=M

@24576
D=D-A
@COLOR_SCREEN
D;JLT

@LOOP
0;JMP // infinite loop
