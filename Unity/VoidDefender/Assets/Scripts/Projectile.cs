using UnityEngine;
using System.Collections;

public class Projectile : MonoBehaviour {

	public float speed, damage;
	private bool hasHit;
	// Use this for initialization
	void Start () {
		hasHit = false;
	}
	
	// Update is called once per frame
	void Update () {
		transform.Translate(Vector3.right * speed * Time.deltaTime);
	
	}

	void OnTriggerEnter2D (Collider2D collider)
	{
		Attacker attacker = collider.gameObject.GetComponent<Attacker>();
		if (!attacker)
		{
			return;
		}
		Health health = collider.gameObject.GetComponent<Health>();
		if (attacker && health && !hasHit)
		{
			hasHit = true;
			health.DealDamage(damage);
			Destroy(gameObject);//destroy self
		}

	}
}
