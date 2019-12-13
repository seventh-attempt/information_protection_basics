using System;
using System.Security.Cryptography;
using System.Windows.Forms;

namespace lab8
{
    class Esign
    {
        public DSAParameters dSA;
        byte[] SignedHash;
        byte[] betHash;
        byte[] hashBytes;
        byte[] sourceHash;

        public int GetKeySize()
        {
            DSACng dsa = new DSACng();
            dsa.ImportParameters(dSA);

            return dsa.KeySize;
        }
        public int GetHashSize()
        {
            return betHash.Length * 8;
        }
        public string GetSource()
        {
            return BitConverter.ToString(this.sourceHash);
        }
        public string GetSeed()
        {
            DSACng dsa = new DSACng();
            dsa.ImportParameters(dSA);

            return BitConverter.ToString(dSA.Seed);
        }
        public string GetSing()
        {
            return BitConverter.ToString(this.SignedHash);
        }
        public byte[] GetHash()
        {
            return this.betHash;
        }
        public int GetSignatureSize()
        {
            return this.SignedHash.Length;
        }

        public void Encode(byte[] oldHash)
        {
            DSACng dsa = new DSACng();
            sourceHash = oldHash;
            DSASignatureFormatter DSAFormatter = new DSASignatureFormatter(dsa); //creating signature and sending keys

            SHA512 sha512 = new SHA512CryptoServiceProvider();
            hashBytes = sha512.ComputeHash(sourceHash);
            this.SignedHash = dsa.SignData(sourceHash, HashAlgorithmName.SHA512);
            DSASignatureDeformatter DSADeformatter = new DSASignatureDeformatter(dsa); // checking signature
            dSA = dsa.ExportParameters(false); // sending open key
        }
        public void CreateHash(byte[] oldHash)
        {
            SHA512 sha512 = new SHA512CryptoServiceProvider();
            betHash = sha512.ComputeHash(oldHash);
        }
        public string VerifSign(byte[] Hash)
        {
            CreateHash(Hash);
            byte[] Hashc = this.betHash;

            DSACng dsa = new DSACng();

            dsa.ImportParameters(dSA);
            DSASignatureDeformatter DSADeformatter = new DSASignatureDeformatter(dsa);

            if (DSADeformatter.VerifySignature(Hashc, this.SignedHash))
            {
                return ("Verified");
            }
            else
            {
                return ("Not verified");
            }
        }
    }

    static class Program
    {
        /// <summary>
        /// Главная точка входа для приложения.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
}
