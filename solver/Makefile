CXX=g++
RM=rm -f
CPPFLAGS=-g -std=c++11
LDFLAGS=-g -std=c++11
LDLIBS=

SRCS=KlondikeSolver.cpp Solitaire.cpp Pile.cpp Card.cpp Move.cpp Random.cpp
OBJS=$(subst .cpp,.o,$(SRCS))

all: KlondikeSolver

KlondikeSolver: $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $(OBJS) $(LDLIBS)

%.o: %.cpp
	$(CXX) $(CPPFLAGS) -c $<

clean:
	$(RM) $(OBJS)

dist-clean: clean
	$(RM) KlondikeSolver
