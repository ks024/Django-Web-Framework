### Regex Meta Characters with Examples

Here's a reference for common regex meta characters, along with examples:

- **`.`**: Matches any single character (except newline).  
  **Example:** `a.b` matches `acb`, `a1b`, but not `ab` or `a\nb`.

- **`^`**: Asserts the start of a line or string.  
  **Example:** `^Hello` matches `Hello, world!` but not `Say Hello`.

- **`$`**: Asserts the end of a line or string.  
  **Example:** `world!$` matches `Hello, world!` but not `world! Hello`.

- **`*`**: Matches 0 or more occurrences of the preceding element.  
  **Example:** `a*` matches `""` (empty), `a`, `aa`, `aaa`.

- **`+`**: Matches 1 or more occurrences of the preceding element.  
  **Example:** `a+` matches `a`, `aa`, `aaa` but not `""`.

- **`?`**: Matches 0 or 1 occurrence of the preceding element (optional).  
  **Example:** `colou?r` matches `color` and `colour`.

- **`{n}`**: Matches exactly `n` occurrences of the preceding element.  
  **Example:** `a{3}` matches `aaa` but not `aa` or `aaaa`.

- **`{n,}`**: Matches `n` or more occurrences of the preceding element.  
  **Example:** `a{2,}` matches `aa`, `aaa`, but not `a`.

- **`{n,m}`**: Matches between `n` and `m` occurrences of the preceding element.  
  **Example:** `a{2,4}` matches `aa`, `aaa`, `aaaa` but not `a` or `aaaaa`.

- **`[]`**: Defines a character class, matching any single character within the brackets.  
  **Example:** `[abc]` matches `a`, `b`, or `c`.

- **`|`**: Acts as a logical OR between expressions.  
  **Example:** `cat|dog` matches `cat` or `dog`.

- **`()`**: Groups patterns and captures matched text.  
  **Example:** `(abc)+` matches `abc`, `abcabc`, `abcabcabc`.

- **`\`**: Escapes a meta character, allowing it to be treated as a literal character.  
  **Example:** `\.` matches the period character `.`.
