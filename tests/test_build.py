"""
Tests for the build script.

This module tests the static site generation functionality.
"""

import os
import sys
from pathlib import Path
import tempfile
import shutil

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest


def test_build_script_imports():
    """Test that build script can be imported."""
    import build
    assert hasattr(build, 'build_static_site')
    assert hasattr(build, 'update_asset_paths')
    assert hasattr(build, 'copy_static_assets')


def test_update_asset_paths():
    """Test asset path update function."""
    from build import update_asset_paths
    
    html = '<link rel="stylesheet" href="/static/css/style.css">'
    base_url = '/'
    
    result = update_asset_paths(html, base_url)
    
    assert '/static/css/style.css' in result


def test_update_navigation_links():
    """Test navigation link updates."""
    from build import update_asset_paths
    
    html = '<a href="/resources">Resources</a>'
    base_url = '/'
    
    result = update_asset_paths(html, base_url)
    
    assert '/resources.html' in result


def test_build_static_site_creates_directory():
    """Test that build creates output directory."""
    from build import build_static_site
    
    # Use temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, 'test_output')
        
        # Build site
        build_static_site(output_dir=output_dir)
        
        # Check directory exists
        assert os.path.exists(output_dir)
        
        # Check files were created
        assert os.path.exists(os.path.join(output_dir, 'index.html'))
        assert os.path.exists(os.path.join(output_dir, 'resources.html'))
        assert os.path.exists(os.path.join(output_dir, 'static'))


def test_build_creates_required_pages():
    """Test that all required pages are created."""
    from build import build_static_site
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, 'test_output')
        build_static_site(output_dir=output_dir)
        
        required_pages = [
            'index.html',
            'resources.html',
            'examples.html',
            'about.html',
            'author.html',
            'tutorials.html',
            '404.html',
        ]
        
        for page in required_pages:
            page_path = os.path.join(output_dir, page)
            assert os.path.exists(page_path), f"Page {page} not created"


def test_static_assets_copied():
    """Test that static assets are copied."""
    from build import build_static_site
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, 'test_output')
        build_static_site(output_dir=output_dir)
        
        # Check static directory exists
        static_dir = os.path.join(output_dir, 'static')
        assert os.path.exists(static_dir)
        
        # Check CSS and JS directories
        assert os.path.exists(os.path.join(static_dir, 'css'))
        assert os.path.exists(os.path.join(static_dir, 'js'))


def test_generated_html_has_correct_paths():
    """Test that generated HTML has correct asset paths."""
    from build import build_static_site
    
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, 'test_output')
        base_url = '/'
        build_static_site(output_dir=output_dir, base_url=base_url)
        
        # Read generated index.html
        index_path = os.path.join(output_dir, 'index.html')
        with open(index_path, 'r') as f:
            content = f.read()
        
        # Check for correct paths
        assert '/static/' in content
        assert '/resources.html' in content
