# Calculating Execution Time

A Python script that measures the execution time of a program — demonstrated here with an acronym generator using `time.time()`.

## Example

```
AI
Execution Time :  2.5033950805664062e-05
```

## Technologies

- Python 3

## Getting Started

```bash
python code.py
```

## Improvements

- Fixed bug: `a = " "` (leading space) → `a = ""` — output was `" AI"` instead of `"AI"`
- Removed redundant `str()` call: `str(i[0]).upper()` → `i[0].upper()`
- Wrapped logic in `main()` + added `if __name__ == '__main__'` guard

## License

MIT
