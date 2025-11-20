"""
Build script to generate static HTML files from Flask templates.

This script renders all Flask routes to static HTML files for GitHub Pages hosting,
preserving the look and functionality of the application.
"""

import os
import sys
import shutil
from pathlib import Path
from urllib.parse import urljoin

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import create_app


def build_static_site(output_dir: str = 'docs', base_url: str = '/') -> None:
    """
    Build static site by rendering all Flask routes to HTML files.

    Args:
        output_dir: Directory to output static files (default: 'docs' for GitHub Pages).
        base_url: Base URL for the site (default: '/' for custom domain).

    Returns:
        None
    """
    # Create Flask app
    app = create_app()
    app.config['FREEZER_BASE_URL'] = base_url
    app.config['FREEZER_RELATIVE_URLS'] = False

    # Create output directory
    output_path = Path(output_dir)
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True)

    # Routes to render
    routes = [
        ('/', 'index.html'),
        ('/resources', 'resources.html'),
        ('/examples', 'examples.html'),
        ('/about', 'about.html'),
        ('/author', 'author.html'),
        ('/tutorials', 'tutorials.html'),
        ('/copilot-integration', 'copilot-integration.html'),
        ('/404', '404.html'),
    ]

    # Render each route
    with app.test_client() as client:
        for route, filename in routes:
            print(f"Rendering {route} -> {filename}")
            try:
                response = client.get(route)
                # Accept both 200 and 404 status codes (for error pages)
                if response.status_code in (200, 404):
                    html = response.data.decode('utf-8')
                    
                    # Update asset paths for GitHub Pages
                    html = update_asset_paths(html, base_url)
                    
                    # Write to file
                    output_file = output_path / filename
                    output_file.write_text(html, encoding='utf-8')
                    print(f"  ✓ Created {output_file}")
                else:
                    print(f"  ✗ Error: {response.status_code}")
            except Exception as e:
                print(f"  ✗ Error rendering {route}: {e}")

    # Copy static assets
    copy_static_assets(output_path, base_url)
    
    # Create CNAME file for custom domain
    create_cname_file(output_path)
    
    # Create .nojekyll file to disable Jekyll processing
    create_nojekyll_file(output_path)

    print(f"\n✓ Static site built successfully in '{output_dir}' directory")
    print(f"  Base URL: {base_url}")
    print(f"  Files generated: {len(list(output_path.rglob('*')))}")


def update_asset_paths(html: str, base_url: str) -> str:
    """
    Update asset paths in HTML to work with GitHub Pages.

    Args:
        html: HTML content to update.
        base_url: Base URL for the site.

    Returns:
        Updated HTML content.
    """
    # Update asset references
    html = html.replace('href="/static/', f'href="{base_url}static/')
    html = html.replace('src="/static/', f'src="{base_url}static/')
    
    # Update navigation links
    html = html.replace('href="/"', f'href="{base_url}"')
    html = html.replace('href="/resources"', f'href="{base_url}resources.html"')
    html = html.replace('href="/examples"', f'href="{base_url}examples.html"')
    html = html.replace('href="/about"', f'href="{base_url}about.html"')
    html = html.replace('href="/author"', f'href="{base_url}author.html"')
    html = html.replace('href="/tutorials"', f'href="{base_url}tutorials.html"')
    html = html.replace('href="/copilot-integration"', f'href="{base_url}copilot-integration.html"')
    
    return html


def copy_static_assets(output_path: Path, base_url: str) -> None:
    """
    Copy static assets (CSS, JS) to output directory.

    Args:
        output_path: Path to output directory.
        base_url: Base URL for the site.

    Returns:
        None
    """
    src_static = Path('src/static')
    dest_static = output_path / 'static'

    if src_static.exists():
        print(f"\nCopying static assets...")
        shutil.copytree(src_static, dest_static, dirs_exist_ok=True)
        print(f"  ✓ Copied static assets to {dest_static}")
        
        # Count files
        css_files = list(dest_static.glob('**/*.css'))
        js_files = list(dest_static.glob('**/*.js'))
        print(f"  - CSS files: {len(css_files)}")
        print(f"  - JS files: {len(js_files)}")


def create_cname_file(output_path: Path) -> None:
    """
    Create CNAME file for GitHub Pages custom domain.

    Args:
        output_path: Path to output directory.

    Returns:
        None
    """
    cname_file = output_path / 'CNAME'
    cname_file.write_text('copilot.agharib.com\n', encoding='utf-8')
    print(f"\n✓ Created CNAME file for custom domain: copilot.agharib.com")


def create_nojekyll_file(output_path: Path) -> None:
    """
    Create .nojekyll file to disable Jekyll processing on GitHub Pages.

    Args:
        output_path: Path to output directory.

    Returns:
        None
    """
    nojekyll_file = output_path / '.nojekyll'
    nojekyll_file.write_text('', encoding='utf-8')
    print(f"✓ Created .nojekyll file to disable Jekyll processing")


if __name__ == '__main__':
    # Check if custom output directory specified
    output_dir = sys.argv[1] if len(sys.argv) > 1 else 'docs'
    
    # Build the static site
    build_static_site(output_dir=output_dir)
