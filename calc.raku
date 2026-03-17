#!/usr/bin/env raku

LOOP: loop {
	my @stack;

	for get.words -> $t {
		with try $t.Int { @stack.push: $_; next }
		@stack.elems >= 2 or (say "Too Few Arguments"; next LOOP);
		
		my ($b, $a) = @stack.pop, @stack.pop;

		@stack.push: do given $t {
			when "+" { $a + $b }
			when "-" { $a - $b }
			when "*" { $a * $b }
			when "/" { $a / $b }
			default  { say "Invalid Token"; next LOOP }
		}
	}

	say @stack.elems eq 1 ?? @stack[0] !! "Invalid Input";
}
