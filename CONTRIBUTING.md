# Contribuer

- ## Authentification

Une authentification à 2 facteurs est mise en place grâce à django-otp et les EmailDevice

Workflow:

- L'utilisateur se connecte normalement avec email/mdp (user.is_authenticated est True)
- Un email contenant un code secret lui est adressé, le code a une durée de vie de `OTP_EMAIL_TOKEN_VALIDITY` secondes (10 mn par défaut)
- Il est dirigé vers la page du second facteur
- Il renseigne le code reçu. Il est désormais vérifié ( user.is_verified() est True )
- Les views à protéger héritent de SecondFactorMixin qui requiert un user vérifié
- L'admin django est également protégé
- L'utilisateur peut demander un renvoi de code. L'envoi est throttlé (`OTP_EMAIL_THROTTLE_DELAY` secondes) via une key redis pour éviter les abus.