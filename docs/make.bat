@echo off
REM Makefile for Windows

set SPHINXBUILD=sphinx-build
set SOURCEDIR=.
set BUILDDIR=_build

if "%1" == "clean" (
    rmdir /S /Q %BUILDDIR%
    goto end
)

if "%1" == "html" (
    %SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR%
    goto end
)

echo.
echo Usage: make [clean|html]
echo.

:end
