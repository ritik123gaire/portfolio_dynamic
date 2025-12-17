"""
Generate a secure Django SECRET_KEY
Run this and use the output in your environment variables
"""
from django.core.management.utils import get_random_secret_key

print("\n" + "="*60)
print("🔐 Your Django SECRET_KEY:")
print("="*60)
print(get_random_secret_key())
print("="*60)
print("\n💡 Copy this and add it to your Railway environment variables:")
print("   Variable name: DJANGO_SECRET_KEY")
print("   Variable value: (paste the key above)")
print("\n⚠️  Keep this secret! Don't commit it to GitHub!\n")
