export const metadata = {
  title: 'TradeGuard MT5',
  description: 'SaaS trade management + journal analytics for MT5',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  )
}
