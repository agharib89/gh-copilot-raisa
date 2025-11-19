---
description: 'Performance optimization guidelines for Python'
applyTo: '**/*.py'
---

# Performance Optimization Guidelines

## General Principles

- Measure before optimizing - use profiling tools to identify bottlenecks.
- Prioritize code readability unless performance is critical.
- Optimize algorithms and data structures before micro-optimizations.
- Consider the trade-offs between performance and maintainability.

## Data Structures

- Choose appropriate data structures for your use case.
- Use `set` for membership testing instead of `list`.
- Use `dict` for fast key-value lookups.
- Consider `collections.deque` for efficient queue operations.
- Use `collections.defaultdict` and `collections.Counter` for common patterns.

## Algorithms

- Prefer built-in functions and methods - they're typically optimized.
- Use list comprehensions instead of loops when appropriate.
- Consider generator expressions for large datasets to save memory.
- Use `itertools` for efficient iteration patterns.
- Choose appropriate sorting algorithms and leverage `sorted()` and `.sort()`.

## String Operations

- Use `str.join()` for concatenating multiple strings.
- Avoid repeated string concatenation in loops.
- Use f-strings for string formatting (they're faster than `%` or `.format()`).
- Consider `io.StringIO` for building large strings.

## Function Optimization

- Use `functools.lru_cache` for memoization of pure functions.
- Minimize function call overhead in tight loops.
- Use local variables instead of global lookups in performance-critical code.
- Consider using default arguments instead of repeated conditional logic.

## I/O Operations

- Use buffered I/O for file operations.
- Batch database operations when possible.
- Use connection pooling for database connections.
- Consider asynchronous I/O with `asyncio` for I/O-bound operations.
- Cache expensive I/O results when appropriate.

## Memory Management

- Use generators for processing large sequences.
- Be mindful of memory leaks with circular references.
- Use `__slots__` for classes with many instances.
- Consider using `array.array` for large numeric arrays.
- Use context managers to ensure proper resource cleanup.

## Concurrency and Parallelism

- Use `asyncio` for I/O-bound concurrent operations.
- Use `multiprocessing` for CPU-bound parallel operations.
- Consider `concurrent.futures` for simple parallelization.
- Be aware of the Global Interpreter Lock (GIL) limitations.
- Use thread-safe data structures when working with threads.

## Library Choices

- Use NumPy for numerical computations.
- Use pandas for data manipulation and analysis.
- Consider Cython or PyPy for performance-critical code.
- Use compiled extensions when native Python is too slow.

## Profiling and Benchmarking

- Use `cProfile` or `profile` for profiling.
- Use `timeit` for micro-benchmarks.
- Use memory profilers like `memory_profiler` for memory analysis.
- Profile in realistic conditions with representative data.

## Database Optimization

- Use appropriate database indexes.
- Batch INSERT/UPDATE operations.
- Use query optimization techniques.
- Consider database connection pooling.
- Use lazy loading for large object graphs.

## Best Practices

- Don't optimize prematurely - profile first.
- Focus on algorithmic improvements over micro-optimizations.
- Document any performance-critical code sections.
- Balance performance with code maintainability.
- Set performance benchmarks and monitor regressions.
