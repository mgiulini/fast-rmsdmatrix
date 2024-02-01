# makefile for fast-rmsdmatrix

# Compiler

CC = gcc

# Compiler flags

CFLAGS = -Wall -O3 -march=native -std=c99

# Linker flags

LDFLAGS = -lm

# Source files

SRC = fast-rmsdmatrix.c

# Object files

OBJ = $(SRC:.c=.o)

# Executable

EXEC = fast-rmsdmatrix

# Default target

all:
	make $(EXEC)

# Clean

clean:
	rm -f $(OBJ) $(EXEC)