"""
SELECT TenantName
FROM Tenants
INNER JOIN ( SELECT TenantID FROM AptTenant GROUP BY TenantID Having COUNT(*) >= 2 ) foo
ON foo.TenantID = Tenants.TenantID
"""
