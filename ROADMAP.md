# Roadmap

Not scheduled. Ideas for later, in order.

1. **Flexible splits:** split unevenly (e.g. 70/30) and leave
   people out of some items.
   Needs: new data model (items → who shares, in what ratio), more tests.
   Works in the CLI; no web app needed.

2. **Bill upload:** upload a photo or PDF of a bill; the items are read automatically.
   Needs: web app, file storage, LLM to extract items (Week 2 skills).

3. **Easy payment:** one tap to pay a flatmate.
   Needs: a payment QR code (GiroCode) or PayPal.me link.
   Not in-app bank payments (PSD2 licensing, real bank data). See ADR-0003.
